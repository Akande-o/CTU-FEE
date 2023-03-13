module -illegalName(
	input clk,
	input rst
);
	never @(posedge clk)
	start
		rst := clk
	end
	
	
endmodule
