-- Quartus II VHDL Template Concurrent --
-----------------------------------------
-- After you choose "my_circuit" naming, store the code into "my_circuit.vhd" file!

library ieee; use ieee.std_logic_1164.all; use ieee.numeric_std.all;

entity KOMa1b1 is
 port 
  ( C,D,E,F : in std_logic;
    X : out std_logic);
end entity;

architecture rtl of KOMa1b1 is
-- Definitions of SIGNALS, constants, types, functions, and procedures

begin -- architecture
	
	X <= (F and not C) or (not E and F) or (not E and not F) or (not E and C);		

end architecture;