library verilog;
use verilog.vl_types.all;
entity BeaconAE is
    port(
        X0              : in     vl_logic;
        X1              : in     vl_logic;
        X2              : in     vl_logic;
        X3              : in     vl_logic;
        X4              : in     vl_logic;
        X5              : in     vl_logic;
        STOP            : out    vl_logic;
        Y               : out    vl_logic
    );
end BeaconAE;
