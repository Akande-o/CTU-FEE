-- Quartus II VHDL Template Concurrent --
-----------------------------------------
-- After you choose "my_circuit" naming, store the code into "my_circuit.vhd" file!

library ieee; use ieee.std_logic_1164.all; use ieee.numeric_std.all;

entity BeaconAX is
 port 
  ( A,B,C,D : in std_logic;
    M : out std_logic);
end entity;

architecture rtl of BeaconAX is

-- Definitions of SIGNALS, constants, types, functions, and procedures

begin -- architecture

	M <= (A and D) or (not B and C);

end architecture;
