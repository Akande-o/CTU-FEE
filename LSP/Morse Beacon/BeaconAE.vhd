-- Quartus II VHDL Template Concurrent --
-----------------------------------------
-- After you choose "my_circuit" naming, store the code into "my_circuit.vhd" file!

library ieee; use ieee.std_logic_1164.all; use ieee.numeric_std.all;

entity BeaconAE is
 port 
  ( X0, X1, X2, X3, X4, X5 : in std_logic;
    STOP,Y : out std_logic);
end entity;

architecture rtl of BeaconAE is
signal A,B,C,D,E,F :std_logic;
signal Y00, Y01, Y10, Y11 : std_logic;
-- Definitions of SIGNALS, constants, types, functions, and procedures

begin -- architecture
	A <= X5; B <= X4; C <= X3; D <= X2; E <= X1; F <= X0;
	Y00 <= (E and not D) or (F and not D) or (E and not C and D) or (F and not C and D) or (E and F);
	Y01 <= (E and F) or (F and D) or (E and C and D) or (E and not C and not D) or (F and not C and not D);
	Y10 <= (F and D) or (not E and C and D) or (E and F);
	Y11 <= (not C and not E) or (not C and not D and F);
	
	
	Y <=	 (not A and not B and Y00)
		 or (not A and B and Y01)
		 or (A and not B and Y10)
		 or (A and B and Y11);
	STOP <= A and B and D and E and F;
			

end architecture;
