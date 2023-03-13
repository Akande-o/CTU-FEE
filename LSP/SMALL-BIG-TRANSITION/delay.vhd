library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity delay is
    port (
        clk : in  std_logic;
        start : in  std_logic;
		  large_flag : in std_logic;
		  wait_time : in std_logic;
        done : out  std_logic
    );
end delay;

architecture delay_behavioral of delay is
    constant delay_period : integer := 240; -- 3 seconds delay
	 constant short_delay_period : integer := 120; -- 1 second delay
    signal count : integer range 0 to 240 := 0;
begin
    process (clk)
    begin
        if rising_edge(clk) then
            if start = '1' then
                if (wait_time = '1' and large_flag = '1') then
                    if count = short_delay_period then
                        count <= 0;
                        done <= '1';
                    else
                        count <= count + 1;
								done <= '0';
                    end if;
                else
                    if count = delay_period then
                        count <= 0;
                        done <= '1';
                    else
                        count <= count + 1;
								done <= '0';
                    end if;
                end if;
            else
                count <= 0;
					 done <= '1';
            end if;
        end if;
    end process;
end delay_behavioral;