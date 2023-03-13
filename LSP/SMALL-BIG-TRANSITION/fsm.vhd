library ieee;
use ieee.std_logic_1164.all;

entity fsm is
    port ( input_value : in  std_logic;
           clk : in  std_logic;
			  response : in  std_logic;
			  effect_done : in std_logic;
			  large_flag : out std_logic;
           current_state : out  std_logic_vector (1 downto 0);
	        delay_trigger : out std_logic;
			  effect_start : out std_logic;
			  move_start : out std_logic;
			  effect_output : out std_logic
			  );
end fsm;

architecture fsm_behavioral of fsm is
    type state_type is (state_1, state_2);
    signal current_state_sig : state_type := state_2;
	 signal next_state_sig : state_type := state_1;
	 signal start_up : integer := 1; 
begin
    -- state transitions
    process (clk)
    begin
        if rising_edge(clk) then
            if (response = '1' or start_up = 1) then
				    start_up <= 0;
					 if current_state_sig /= next_state_sig then
					     if current_state_sig = state_1 then
						      large_flag <= '0';
								move_start <= '1';
						  else
						      large_flag <= '1';
								move_start <= '0';
						  end if;
					     effect_output <= input_value;
					     delay_trigger <= '1';
					     effect_start <= '1';
					     current_state_sig <= next_state_sig;
					 else
					     delay_trigger <= '0';
					 end if;
					
					 --if next_state_sig = state_2 then
					 --    large_flag <= '1';
					 --else
					 --    large_flag <= '0';
					 --end if;
            end if;
				--if effect_done = '1' then
				--    delay_trigger <= '1';
				--	 effect_start <= '0';
			   --end if;
        end if;
    end process;

    -- state transition logic
    process (input_value, current_state_sig)
    begin
        case current_state_sig is
            when state_1 =>
				    next_state_sig <= state_2; -- big flag
            when state_2 =>
                next_state_sig <= state_1; -- small flag
        end case;
    end process;

    -- output current state
    current_state <= "00" when current_state_sig = state_1 else
                   "01" when current_state_sig = state_2 else
                   "XX";
end fsm_behavioral;