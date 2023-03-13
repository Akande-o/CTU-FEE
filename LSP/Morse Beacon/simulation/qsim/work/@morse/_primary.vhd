library verilog;
use verilog.vl_types.all;
entity Morse is
    port(
        Sound           : out    vl_logic;
        CLOCK_50        : in     vl_logic;
        SW              : in     vl_logic_vector(1 downto 0);
        KEY             : in     vl_logic_vector(0 downto 0);
        LEDR            : out    vl_logic_vector(17 downto 0)
    );
end Morse;
