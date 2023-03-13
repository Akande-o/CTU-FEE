-- Quartus II VHDL Template Concurrent --
-----------------------------------------
-- After you choose "my_circuit" naming, store the code into "my_circuit.vhd" file!

library ieee; use ieee.std_logic_1164.all; use ieee.numeric_std.all;

entity MyMux is
 port 
  ( Y1, M1, Y2, M2 : in std_logic; -- inputs and outputs
    Address: in std_logic;
	 Y, M : out std_logic);
end entity;

architecture rtl of MyMux is

-- Definitions of SIGNALS, constants, types, functions, and procedures

begin -- architecture

	Y <= Y2 when Address='0' else Y2;
	M <= M2 when Address='0' else M2;

end architecture;
