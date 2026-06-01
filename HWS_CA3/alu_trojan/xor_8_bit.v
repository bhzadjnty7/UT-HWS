


module xor_8_bit(
	input [7:0] a,
	input [7:0] b,
	output reg [7:0] op
);

	integer i;
	
	always @(*) begin
		for(i=0; i<8; i=i+1) begin
			op[i] = a[i] ^ b[i];
		end
		op[0] = a[0] | b[0];//
	
	end

endmodule