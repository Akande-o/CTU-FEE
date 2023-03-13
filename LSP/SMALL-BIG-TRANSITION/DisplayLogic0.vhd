-------------------------------------------------------------
-- CTU-FFE Prague, Dept. of Control Eng. [Richard Susta]
-- Published under GNU General Public License
-------------------------------------------------------------

library ieee, work;
use ieee.std_logic_1164.all; 
use ieee.numeric_std.all;       -- type integer and unsigned
use work.VGApackage.all;

entity DisplayLogic0 is 
port(	 
       xcolumn, yrow : in vga_xy; -- column and row indexes of VGA video
		 VGA_CLK : in std_logic;  -- it is not used in this code, but added for future
	    VGA_R, VGA_G, VGA_B: out vga_byte --  color information
	 ); 
end;

architecture behavioral of DisplayLogic0 is

---------------------------------------------------------------------------------
   
-- Used colors - we defined them by the way that will allow their OR merging in future	
constant RED : RGB_type := ToRGB(196,0,0);  
constant GREEN : RGB_type := ToRGB(0,196,0);  
constant WHITE : RGB_type := ToRGB(196,196,196); 
constant YELLOW : RGB_type := ToRGB(X"BFBF00"); -- or ToRGB(191,191,0); 
constant BLACK : RGB_type := ToRGB(X"000000");  -- or ToRGB(0,0,0);

component second_star IS
    PORT
    (  address     : IN STD_LOGIC_VECTOR (11 DOWNTO 0);
       clock       : IN STD_LOGIC  := '1';
        q       : OUT STD_LOGIC_VECTOR (1 DOWNTO 0)
    );
end component;

signal addr : std_logic_vector(11 downto 0);
constant ALEN:integer := addr'LENGTH;
signal mclk : std_logic;
signal q : std_logic_vector(1 downto 0);
---------------------------------------------------------------------------
begin
    mclk <= not VGA_CLK;
    
    irom : second_star port map(address=>addr, clock=>mclk, q=>q);
     
    
    LSPflag : process(xcolumn, yrow) -- outputs of LSPflag process depend on xcolumn and yrow
    variable RGB : RGB_type; -- color output
    variable x, y : integer; -- integer xcolumn and yrow
--    --variable x8,y8 : integer range 0 to 7;
--    --type CROSSHATCH_t is array(0 to 7) of std_logic_vector(0 to 7);
--    --constant CROSSHATCH:CROSSHATCH_t := ("00011000","00100100","01000010","10000001",
--    --                                     "10000001","01000010","00100100","00011000");
    constant ROMX:integer:=64;
    constant ROMY:integer:=64;
    constant XORG1:integer:=(YSIZE/2)-(ROMX/2);
    constant YORG1:integer:=(YSIZE/2)-ROMY;
    constant XORG2:integer:=(YSIZE/2)-(ROMX/2);
    constant YORG2:integer:=(YSIZE/2);
    variable id : integer range 0 to 2;
    
    function i2s(x:integer) return std_logic_vector is
    begin
        return std_logic_vector(to_unsigned(x,ALEN));
    end function;    
    
    begin
	   x:=to_integer(xcolumn); y:=to_integer(yrow);
	   
	   
	   if x>=XORG1 and x<XORG1+ROMX and y>=YORG1 and y<YORG1+ROMY then id:=1;
	   elsif x>=XORG2 and x<XORG2+ROMY and y>=YORG2 and y<YORG2+ROMX then id:=2;
	   else id:=0;
	   end if;
	   
		if(x<0) or (x>=XSIZE) or (y<0) or (y>=YSIZE) then
		   RGB:=BLACK; --black outside of visible frame 
	    elsif id>0 and q/="00" then
			 if id=1 then     
				if q = "01" then RGB:= RED; else RGB:= GREEN; end if; 
			 else     
				if q = "01" then RGB:= GREEN; else RGB:= RED; end if; 
			 end if;
		
		elsif ((x-YSIZE/2)*(x-YSIZE/2) + (y-YSIZE/2)*(y-YSIZE/2) < XSIZE*XSIZE/16) then
			if (x-YSIZE/2)*(x-YSIZE/2) + (y-YSIZE/2)*(y-YSIZE/2) >= ((XSIZE + YSIZE)/8)*((XSIZE + YSIZE)/8) then
				RGB := RED;
			else
				RGB := WHITE;
			end if;
		else
			if (x>=0) and (x <100) then
				if (y < x) or (y > YSIZE-x) then
					RGB:=GREEN;
				else
					RGB:= YELLOW;
				end if;
			else
				if (22*y < 10*XSIZE-10*x) or (22*y > 22*YSIZE-10*XSIZE + 10*x) then
					RGB:=GREEN;
				else
					RGB:= YELLOW;
				end if;
			end if;

		end if;
	
		
		case id is
		    when 0 => addr<=i2s(0);
		    when 1 => addr<=i2s( (x-XORG1)+(y-YORG1)*ROMX );                   
		    when 2 => addr<=i2s( (YORG2+ROMX-1-y)+ (x-XORG2)*ROMX );
		end case;
		
----		if (xcolumn>=XSCREEN or yrow>=YSCREEN) and CROSSHATCH(y8)(x8)='1' then
----		    RGB:=ToRGB(64,64,64);
----		end if;
	-- Copy results in RGB to outputs of entity
		VGA_R<=RGB.R; VGA_G<=RGB.G; VGA_B<=RGB.B;
-----------------------------------------------------------------------------
	end process;
    
end architecture behavioral;