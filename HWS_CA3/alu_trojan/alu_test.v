
// GroupID-73(15116003_15116066) - Abhimanyu Bambhaniya & Utkarsh Gupta 
// Date: October 27, 2016 

module alu_test;

	// Inputs
	reg [7:0] a;
	reg [7:0] b;
	reg [1:0] op_code;

	// Outputs
	wire [15:0] out;
	wire overflow;
	wire c_out;
	integer fout;

	// Instantiate the Unit Under Test (UUT)
	alu uut (
		.a(a), 
		.b(b), 
		.op_code(op_code), 
		.out(out), 
		.overflow(overflow), 
		.c_out(c_out)
	);

	initial begin
		// Initialize Inputs
		a = 0;
		b = 0;
		op_code = 0;

	end
	initial begin
    fout = $fopen("alu_test_trojan.txt", "w");
    if(fout==0) $finish;
    $fwrite(fout, "Results
=======================
"); end

	always begin
		#100 a = 45; b = 61; op_code = 2'b00;
		$fwrite(fout, "Test %0d: a=%d, b=%d, op=%d => out=%d, c_out=%d, overflow=%d\n", 23, a, b, op_code, out, c_out, overflow);
		#100 a = 45; b = 61; op_code = 2'b01;
		$fwrite(fout, "Test %0d: a=%d, b=%d, op=%d => out=%d, c_out=%d, overflow=%d\n", 23, a, b, op_code, out, c_out, overflow);
		#100 a = 45; b = 61; op_code = 2'b11;
		$fwrite(fout, "Test %0d: a=%d, b=%d, op=%d => out=%d, c_out=%d, overflow=%d\n", 23, a, b, op_code, out, c_out, overflow);
		#100 a = 45; b = 61; op_code = 2'b10;
		$fwrite(fout, "Test %0d: a=%d, b=%d, op=%d => out=%d, c_out=%d, overflow=%d\n", 23, a, b, op_code, out, c_out, overflow);
		$fwrite(fout, "=======================\nAll tests applied.\n");
    $fclose(fout); $stop;
    end     
endmodule

