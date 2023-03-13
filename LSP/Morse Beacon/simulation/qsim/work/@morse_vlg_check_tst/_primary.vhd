library verilog;
use verilog.vl_types.all;
entity Morse_vlg_check_tst is
    port(
        LEDR            : in     vl_logic_vector(17 downto 0);
        Sound           : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end Morse_vlg_check_tst;
