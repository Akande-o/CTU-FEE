library ieee, work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;       -- type integer and unsigned
use work.VGApackage.all;


entity box_mux2 is
    port(
        clk : in std_logic;
        x_in, y_in : in vga_xy;
		  state_in : in std_logic_vector(1 downto 0);
		  effect_start : in std_logic;
		  effect_input : in std_logic;
        output : out integer range 0 to 800;
		  effect_done : out std_logic;
		  effect_output : out std_logic;
		  fade_output : out unsigned(7 downto 0);
		  state_out : out std_logic_vector(1 downto 0);
		  box_out : out integer range 0 to 51
    );
end box_mux2;

architecture behavioral2 of box_mux2 is

constant FRAME_H : integer := 600; -- HEIGHT
constant FRAME_W : integer := 800; -- WIDTH

signal counter : integer range 0 to 600 := 0;
signal box_counter : integer range 0 to 51 := 0;
signal fade_counter : unsigned(7 downto 0) := (others => '0');

begin
    process(clk)
    begin
        if (falling_edge(clk)) then
		      if state_in = "01" then
				    if effect_input = '0' then -- effect 1
					     if (counter < 600) then
					         counter <= counter + 15;
                    end if;
					     --effect_done <= '1';
			       else -- effect 2
					     --if (fade_counter < 255) then
					     --    fade_counter <= fade_counter + 5;
                    --end if;
						  if (box_counter < 51) then
					         box_counter <= box_counter + 1;
                    end if;
					     --effect_done <= '1';
			       end if;
				else -- effect 1
				    if effect_input = '0' then  
					     if (counter > 0) then
					         counter <= counter - 15;
                    end if;
					     --effect_done <= '1';
			       else -- effect 2
					     --if (fade_counter > 0) then
					     --    fade_counter <= fade_counter - 5;
                    --end if;
						  if (box_counter > 0) then
					         box_counter <= box_counter - 1;
                    end if;
					     --effect_done <= '1';
			       end if;
				end if;
        end if;
		  if (counter > 600) then
	         counter <= 600;
		  end if;
	     if (counter < 0) then
	         counter <= 0;
	     end if;
		  if (fade_counter > 255) then
		      fade_counter <= "11111111";
		  end if;
		  if (fade_counter < 0) then
		      fade_counter <= "00000000";
		  end if;
		  if (box_counter > 51) then
	         box_counter <= 51;
		  end if;
		  if (box_counter < 0) then
		      box_counter <= 0;
		  end if;
    end process;
	 -- (x_in >= 50 - box_size/2) and (x_in <= 50 + box_size/2) and (y_in >= 50 - box_size/2) and (y_in <= 50 + box_size/2)
	 state_out <= state_in;
	 output <= counter;
	 fade_output <= fade_counter;
	 box_out <= box_counter;
	 effect_output <= effect_input;
end behavioral2;