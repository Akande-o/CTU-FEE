library ieee, work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;       -- type integer and unsigned
use work.VGApackage.all;

entity movement is
    port(
        clock      : in std_logic;
        x          : in vga_xy;
        y          : in vga_xy;
		  move_start : in std_logic;
		  xcolumn_out, yrow_out : out vga_xy
    );
end movement;

architecture behavioral of movement is
    signal x_dir : integer := -4;
    signal y_dir : integer := -4;
    signal x_pos : integer := 0;
    signal y_pos : integer := 0; 
    signal flag_width : integer := 480; 
    signal flag_height : integer := 320;
	 signal xcounter : integer := 0;
	 signal ycounter : integer := 0;
begin
    process(clock)
    begin
        if (rising_edge(clock) and move_start = '1') then
            x_pos <= x_pos + x_dir;
            y_pos <= y_pos + y_dir;
				xcounter <= xcounter + 1;
				ycounter <= ycounter + 1;

            if (x_pos < -flag_width or x_pos > 0) and xcounter > 50 then
                x_dir <= -x_dir;
					 xcounter <= 0;
            end if;

            if (y_pos < -flag_height or y_pos > 0) and ycounter > 50 then
                y_dir <= -y_dir;
					 ycounter <= 0;
            end if;
        end if;
    end process;
	 
	 xcolumn_out <= x + x_pos;
	 yrow_out <= y + y_pos;
end behavioral;