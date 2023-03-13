library verilog;
use verilog.vl_types.all;
entity BeaconAE_vlg_check_tst is
    port(
        STOP            : in     vl_logic;
        Y               : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end BeaconAE_vlg_check_tst;
