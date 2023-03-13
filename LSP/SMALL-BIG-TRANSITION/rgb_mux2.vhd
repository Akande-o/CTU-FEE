library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use work.VGApackage.all;

entity rgb_mux2 is
    port(
        clk, LCD_DEN_in : IN std_logic;
		  red1,green1,blue1,red2,green2,blue2 : IN vga_byte; -- input colors
		  xcolumn, yrow : in vga_xy;
        input_sel  : in integer range 0 to 800;
		  effect_input : in std_logic;
		  fade_counter : in unsigned(7 downto 0);
		  state_in : in std_logic_vector(1 downto 0);
		  box_counter : in integer range 0 to 51;
  		  red_out,green_out,blue_out : OUT vga_byte; -- output colors
		  LCD_CLK, LCD_DEN : OUT std_logic
    );
end rgb_mux2;

architecture behavioral2 of rgb_mux2 is

function abs_int(x : integer) return integer is
begin
  if x < 0 then
    return -x;
  else
    return x;
  end if;
end function;

begin	 
    process(clk)
	 variable pixel_value : integer;
    variable x_int : integer;
    variable y_int : integer;
	 variable x_box : integer;
    variable y_box : integer;
	 variable local_counter : unsigned(7 downto 0);
	 variable local_box_counter : integer;
	 variable local_box_counter_u : unsigned(7 downto 0);
    begin
        if rising_edge(clk) then
			   x_int := to_integer(xcolumn);
				y_int := to_integer(yrow);
				x_box := x_int mod 100;
				y_box := y_int mod 100;
				if (LCD_DEN_in='1') then
				   if effect_input = '0' then -- effect 1
					    --pixel_value := abs_int((x_int - 400) / 100) * 100 + abs_int((y_int - 300) / 100) * 100;
					    if ((y_int + 3*x_int/4 > 600 - input_sel) and (y_int - 3*x_int/4 < 0 + input_sel) and (y_int + 3*x_int/4 < 600 + input_sel) and (y_int - 3*x_int/4 > 0 - input_sel)) then
				           red_out <= red1;
							  green_out <= green1;
						     blue_out <= blue1;
					    else
						     if ((y_int + 3*x_int/4 > 500 - input_sel*2) and (y_int - 3*x_int/4 < -100 + input_sel*2) and (y_int + 3*x_int/4 < 500 + input_sel*2) and (y_int - 3*x_int/4 > -100 - input_sel*2)) then
								red_out <= std_logic_vector((unsigned(red1) / 2))(7 downto 0);
								green_out <= std_logic_vector((unsigned(green1) / 2))(7 downto 0);
								blue_out <= std_logic_vector((unsigned(blue2) / 2))(7 downto 0);
							  else
							      if ((y_int + 3*x_int/4 > 700 - input_sel*2) and (y_int - 3*x_int/4 < 100 + input_sel*2) and (y_int + 3*x_int/4 < 700 + input_sel*2) and (y_int - 3*x_int/4 > 100 - input_sel*2)) then
								red_out <= std_logic_vector((unsigned(red2) / 2))(7 downto 0);
								green_out <= std_logic_vector((unsigned(green1) / 2))(7 downto 0);
								blue_out <= std_logic_vector((unsigned(blue1) / 2))(7 downto 0);
							  else
								red_out <= red2;
								green_out <= green2;
								blue_out <= blue2;
							  end if;
							  end if;
					    end if;
				   else                       -- effect 2
					    local_box_counter := box_counter * 100;
						 local_box_counter_u := to_unsigned(box_counter, local_box_counter_u'length);
						 if (x_int / 100) mod 2 = 0 then
					    if (x_box - 50)**2 + (y_box - 50)**2 < local_box_counter then
						     --red_out <= std_logic_vector((unsigned(red1) * (unsigned(local_box_counter_u)) + unsigned(red2) * (51 - unsigned(local_box_counter_u))) / 51)(7 downto 0);
  					        --green_out <= std_logic_vector((unsigned(green1) * (unsigned(local_box_counter_u)) + unsigned(green2) * (51 -unsigned(local_box_counter_u))) / 51)(7 downto 0);
                       --blue_out <= std_logic_vector((unsigned(blue1) * (unsigned(local_box_counter_u)) + unsigned(blue2) * (51 -unsigned(local_box_counter_u))) / 51)(7 downto 0);
						     red_out <= red1;
							  green_out <= green1;
						     blue_out <= blue1;
						 else
						     red_out <= red2;
							  green_out <= green2;
						     blue_out <= blue2;
						 end if;
						 else
						 if (x_box - 50)**2 + (y_box - 50)**2 > 5000 - local_box_counter then
						     --red_out <= std_logic_vector((unsigned(red1) * (unsigned(local_box_counter_u)) + unsigned(red2) * (51 - unsigned(local_box_counter_u))) / 51)(7 downto 0);
  					        --green_out <= std_logic_vector((unsigned(green1) * (unsigned(local_box_counter_u)) + unsigned(green2) * (51 -unsigned(local_box_counter_u))) / 51)(7 downto 0);
                       --blue_out <= std_logic_vector((unsigned(blue1) * (unsigned(local_box_counter_u)) + unsigned(blue2) * (51 -unsigned(local_box_counter_u))) / 51)(7 downto 0);
						     red_out <= red1;
							  green_out <= green1;
						     blue_out <= blue1;
						 else
						     red_out <= red2;
							  green_out <= green2;
						     blue_out <= blue2;
						 end if;
						 end if;
--					    if fade_counter mod 5 = 0 then
--							  local_counter := fade_counter;
--						 else
--						     local_counter := fade_counter - (fade_counter mod 5);
--						 end if;
--						 if fade_counter /= 255 then
--						     if fade_counter /= 0 then
--						         red_out <= std_logic_vector((unsigned(red1) * (unsigned(local_counter)) + unsigned(red2) * (255 - unsigned(local_counter))) / 255)(7 downto 0);
--							      green_out <= std_logic_vector((unsigned(green1) * (unsigned(local_counter)) + unsigned(green2) * (255 -unsigned(local_counter))) / 255)(7 downto 0);
--							      blue_out <= std_logic_vector((unsigned(blue1) * (unsigned(local_counter)) + unsigned(blue2) * (255 -unsigned(local_counter))) / 255)(7 downto 0);
--						     else
--							      red_out <= red2;
--						         green_out <= green2;
--							      blue_out <= blue2;
--							  end if;
--						 else
--							  red_out <= red1;
--							  green_out <= green1;
--							  blue_out <= blue1;
--                   end if;
				   end if;
				end if;
        end if;
		  
		  LCD_CLK <= clk;
		  LCD_DEN <= LCD_DEN_in;
    end process;
end behavioral2;