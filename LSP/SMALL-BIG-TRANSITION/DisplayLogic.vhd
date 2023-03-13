-------------------------------------------------------------
-- CTU-FFE Prague, Dept. of Control Eng. [Richard Susta]
-- Published under GNU General Public License
-------------------------------------------------------------

library ieee, work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;       -- type integer and unsigned
use work.VGApackage.all;

entity DisplayLogic is 
port(	xcolumn, yrow : in vga_xy; -- row and  column indexes of VGA video
      VGA_CLK : in std_logic; -- pixel clock
	   VGA_R, VGA_G, VGA_B: out vga_byte	 );  --  color information
end;

architecture behavioral of DisplayLogic is
---------------------------------------------------------------------------------
-- Used colors 	
constant RED : RGB_type := ToRGB(196,0,0);  
constant GREEN : RGB_type := ToRGB(0,96,0);  
constant WHITE : RGB_type := ToRGB(196,196,196);  
constant YELLOW : RGB_type := ToRGB(X"BFBF00"); -- or ToRGB(191,191,0); 
constant BLACK : RGB_type := ToRGB(X"000000");  -- or ToRGB(0,0,0);
---------------------------------------------------------------------------
constant MEMROWSIZE : integer := 128; -- memory organization
constant MEMROWCOUNT : integer := 128;
constant EMBORGX1 : integer := (YSCREEN/2)-(MEMROWSIZE/2); -- positions of picture in the flag
constant EMBORGY1 : integer := (YSCREEN/2)-MEMROWCOUNT;
constant EMBORGX2 : integer := (YSCREEN/2)-(MEMROWSIZE/2); -- positions of picture in the flag
constant EMBORGY2 : integer := (YSCREEN/2);
constant MEM_END_ADDRESS : integer := 4095; -- not used here

component large_star is
    PORT
    (  address     : IN STD_LOGIC_VECTOR (14 DOWNTO 0);
       clock       : IN STD_LOGIC  := '1';
        q       : OUT STD_LOGIC_VECTOR (1 DOWNTO 0)
    );
end component;

signal addr : std_logic_vector(14 downto 0);
constant ALEN:integer := addr'LENGTH;
signal mclk : std_logic;
signal q : std_logic_vector(1 downto 0);

function i2s(x:integer) return std_logic_vector is
    begin
        return std_logic_vector(to_unsigned(x,ALEN));
    end function;
	 
begin
   mclk <= not VGA_CLK;

	rom_inst : large_star port map(address=>addr, clock=>mclk, q=>q);
  
LSPflag : process(xcolumn, yrow, q) -- output of process depends on xcolumn and yrow
    variable RGB : RGB_type; -- output colors
    variable x, y : integer; -- renamed xcolumn and yrow
	 variable romID:integer range 0 to 2;
    begin
		x:=to_integer(xcolumn); y:=to_integer(yrow); -- convert to integer      
		romID:=0;
		if(x>=EMBORGX1 and x<EMBORGX1+MEMROWSIZE 
			and y>=EMBORGY1 and y<EMBORGY1+MEMROWCOUNT) then romID:=1;
		end if;
		
		if(x>=EMBORGX2 and x<EMBORGX2+MEMROWSIZE 
			and y>=EMBORGY2 and y<EMBORGY2+MEMROWCOUNT) then romID:=2;
		end if;
		
		if(x<0) or (x>=XSCREEN) or (y<0) or (y>=YSCREEN) then  RGB:=BLACK; --black outside of visible frame 
		elsif romID>0 and q/="00" then
			 if romID=1 then     
				if q = "01" then RGB:= RED; else RGB:= GREEN; end if; 
			 else     
				if q = "01" then RGB:= GREEN; else RGB:= RED; end if; 
			 end if;
		elsif ((x-YSCREEN/2)*(x-YSCREEN/2) + (y-YSCREEN/2)*(y-YSCREEN/2) < XSCREEN*XSCREEN/16) then
			if (x-YSCREEN/2)*(x-YSCREEN/2) + (y-YSCREEN/2)*(y-YSCREEN/2) >= ((XSCREEN + YSCREEN)/8)*((XSCREEN + YSCREEN)/8) then
				RGB := RED;
			else
				RGB := WHITE;
			end if;
		else
			if (x>=0) and (x <200) then
				if (y < x) or (y > YSCREEN-x) then
					RGB:=GREEN;
				else
					RGB:= YELLOW;
				end if;
			else
				if (22*y < 10*XSCREEN-10*x) or (22*y > 22*YSCREEN-10*XSCREEN + 10*x) then
					RGB:=GREEN;
				else
					RGB:= YELLOW;
				end if;
			end if;

		end if;
	
		case romID is
		    when 0 => addr<=i2s(0);
		    when 1 => addr<=i2s( (x-EMBORGX1)+(y-EMBORGY1)*MEMROWCOUNT );                   
		    when 2 => addr<=i2s( (EMBORGY2+MEMROWCOUNT-1-y)+ (x-EMBORGX2)*MEMROWCOUNT );
		end case;
		-- Copy results in RGB to outputs of entity
		VGA_R<=RGB.R; VGA_G<=RGB.G; VGA_B<=RGB.B;
-----------------------------------------------------------------------------
end process;

end architecture behavioral;
