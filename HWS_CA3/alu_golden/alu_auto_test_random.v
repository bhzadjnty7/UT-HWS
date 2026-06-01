`timescale 1ns / 1ps

module alu_auto_test_random;
  reg [7:0] a;
  reg [7:0] b;
  reg [1:0] op_code;
  wire [15:0] out;
  wire overflow;
  wire c_out;
  alu uut(.a(a), .b(b), .op_code(op_code), .out(out), .overflow(overflow), .c_out(c_out));
  integer fout;
  initial begin
    fout = $fopen("alu_test_results_random.txt", "w");
    if (fout==0) $finish;
    $fwrite(fout, "Results
=======================
");
    #100 a=8'b00001100; b=8'b01111101; op_code=2'b00; // Expected: out=0000000010001001, c_out=0, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 1, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00101100; b=8'b00010000; op_code=2'bxx; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 2, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00001101; b=8'b11010110; op_code=2'b10; // Expected: out=0000000011011011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 3, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00000011; b=8'b01010001; op_code=2'b10; // Expected: out=0000000001010010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 4, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01101110; b=8'b10101100; op_code=2'b11; // Expected: out=0100100111101000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 5, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10110000; b=8'b00010110; op_code=2'b00; // Expected: out=0000000011000110, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 6, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11000001; b=8'b10010110; op_code=2'b10; // Expected: out=0000000001010111, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 7, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00100011; b=8'bxxxxxxxx; op_code=2'b10; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 8, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01110111; b=8'b11000010; op_code=2'b10; // Expected: out=0000000010110101, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 9, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10110101; b=8'b10001000; op_code=2'b00; // Expected: out=0000000000111101, c_out=1, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 10, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01010111; b=8'b01111101; op_code=2'b11; // Expected: out=0010101001111011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 11, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01110000; b=8'b00011100; op_code=2'b00; // Expected: out=0000000010001100, c_out=0, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 12, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11001101; b=8'b01101100; op_code=2'b10; // Expected: out=0000000010100001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 13, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11111111; b=8'b11101010; op_code=2'b01; // Expected: out=0000000011101010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 14, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10000110; b=8'b11011011; op_code=2'b11; // Expected: out=0111001010100010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 15, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01000110; b=8'b00101110; op_code=2'b00; // Expected: out=0000000001110100, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 16, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01010001; b=8'b11011000; op_code=2'b11; // Expected: out=0100010001011000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 17, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11101111; b=8'b00000101; op_code=2'b00; // Expected: out=0000000011110100, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 18, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10001000; b=8'b10101110; op_code=2'b11; // Expected: out=0101110001110000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 19, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00000001; b=8'b10000110; op_code=2'b01; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 20, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00110110; b=8'b10011000; op_code=2'b01; // Expected: out=0000000000010000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 21, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01010010; b=8'b00000000; op_code=2'b11; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 22, a, b, op_code, out, c_out, overflow);

    #100 a=8'bxxxxxxxx; b=8'b10011101; op_code=2'b01; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 23, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00101000; b=8'b11111000; op_code=2'b01; // Expected: out=0000000000101000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 24, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11110011; b=8'b01010100; op_code=2'b11; // Expected: out=0100111110111100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 25, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01100110; b=8'b11001100; op_code=2'b10; // Expected: out=0000000010101010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 26, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11100111; b=8'b01110011; op_code=2'b00; // Expected: out=0000000001011010, c_out=1, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 27, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01110101; b=8'b00000011; op_code=2'b00; // Expected: out=0000000001111000, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 28, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00010000; b=8'b00100100; op_code=2'b10; // Expected: out=0000000000110100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 29, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01101101; b=8'b11110010; op_code=2'b11; // Expected: out=0110011100001010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 30, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01100001; b=8'b11011100; op_code=2'b11; // Expected: out=0101001101011100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 31, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00011011; b=8'b00110010; op_code=2'b10; // Expected: out=0000000000101001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 32, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00110111; b=8'b01100001; op_code=2'b01; // Expected: out=0000000000100001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 33, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10001110; b=8'b00100110; op_code=2'b00; // Expected: out=0000000010110100, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 34, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00000111; b=8'b01111001; op_code=2'b11; // Expected: out=0000001101001111, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 35, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11001101; b=8'b01010100; op_code=2'b11; // Expected: out=0100001101000100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 36, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11101000; b=8'b11111001; op_code=2'b10; // Expected: out=0000000000010001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 37, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00011101; b=8'b00011111; op_code=2'b00; // Expected: out=0000000000111100, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 38, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11110100; b=8'b01010000; op_code=2'b00; // Expected: out=0000000001000100, c_out=1, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 39, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00100011; b=8'b01111000; op_code=2'b01; // Expected: out=0000000000100000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 40, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00010100; b=8'b11010110; op_code=2'b10; // Expected: out=0000000011000010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 41, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01101000; b=8'b10100000; op_code=2'b11; // Expected: out=0100000100000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 42, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10011001; b=8'b00100101; op_code=2'bxx; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 43, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00110011; b=8'b01101101; op_code=2'b01; // Expected: out=0000000000100001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 44, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00100011; b=8'b10111101; op_code=2'b11; // Expected: out=0001100111010111, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 45, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10011010; b=8'b00000100; op_code=2'b10; // Expected: out=0000000010011110, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 46, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00110101; b=8'b01000100; op_code=2'b00; // Expected: out=0000000001111001, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 47, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01001111; b=8'b01101011; op_code=2'b01; // Expected: out=0000000001001011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 48, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10000111; b=8'b10000000; op_code=2'b00; // Expected: out=0000000000000111, c_out=1, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 49, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11011000; b=8'b00010110; op_code=2'bxx; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 50, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10000110; b=8'b11100010; op_code=2'b11; // Expected: out=0111011001001100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 51, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00111001; b=8'b01001100; op_code=2'b10; // Expected: out=0000000001110101, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 52, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01001011; b=8'b00010101; op_code=2'b00; // Expected: out=0000000001100000, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 53, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01101011; b=8'b00110100; op_code=2'b11; // Expected: out=0001010110111100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 54, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01001111; b=8'b01111001; op_code=2'b01; // Expected: out=0000000001001001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 55, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00001100; b=8'b10101010; op_code=2'b11; // Expected: out=0000011111111000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 56, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01111111; b=8'b00110111; op_code=2'b00; // Expected: out=0000000010110110, c_out=0, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 57, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01110001; b=8'b11101011; op_code=2'b01; // Expected: out=0000000001100001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 58, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01100010; b=8'b10001110; op_code=2'b10; // Expected: out=0000000011101100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 59, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11001100; b=8'b10101001; op_code=2'b00; // Expected: out=0000000001110101, c_out=1, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 60, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10000101; b=8'b10000111; op_code=2'bxx; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 61, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10110000; b=8'b10100000; op_code=2'b00; // Expected: out=0000000001010000, c_out=1, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 62, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01100001; b=8'b11011111; op_code=2'bxx; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 63, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01100100; b=8'b00100011; op_code=2'b10; // Expected: out=0000000001000111, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 64, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00111111; b=8'b10011001; op_code=2'b11; // Expected: out=0010010110100111, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 65, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10010111; b=8'b01100010; op_code=2'b11; // Expected: out=0011100111001110, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 66, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01011001; b=8'b10011010; op_code=2'b00; // Expected: out=0000000011110011, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 67, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01101011; b=8'b10100100; op_code=2'b11; // Expected: out=0100010010001100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 68, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11110010; b=8'b01010110; op_code=2'b10; // Expected: out=0000000010100100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 69, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10101011; b=8'b01111000; op_code=2'b01; // Expected: out=0000000000101000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 70, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01001011; b=8'bxxxxxxxx; op_code=2'b11; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 71, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00100101; b=8'b01100011; op_code=2'b11; // Expected: out=0000111001001111, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 72, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01111100; b=8'b00000010; op_code=2'b00; // Expected: out=0000000001111110, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 73, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01110000; b=8'b11101101; op_code=2'b01; // Expected: out=0000000001100000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 74, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00111110; b=8'b11101101; op_code=2'b10; // Expected: out=0000000011010011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 75, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11100010; b=8'b11011010; op_code=2'b11; // Expected: out=1100000001110100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 76, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11110011; b=8'b01111110; op_code=2'b10; // Expected: out=0000000010001101, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 77, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11111000; b=8'b10001100; op_code=2'b10; // Expected: out=0000000001110100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 78, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10101011; b=8'b00101001; op_code=2'b01; // Expected: out=0000000000101001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 79, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01001110; b=8'b00100000; op_code=2'b10; // Expected: out=0000000001101110, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 80, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11010100; b=8'b11010111; op_code=2'b00; // Expected: out=0000000010101011, c_out=1, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 81, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11000010; b=8'b10110100; op_code=2'b11; // Expected: out=1000100001101000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 82, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11010110; b=8'b01110000; op_code=2'b10; // Expected: out=0000000010100110, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 83, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00001110; b=8'b11001111; op_code=2'b11; // Expected: out=0000101101010010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 84, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00001101; b=8'b00001101; op_code=2'b11; // Expected: out=0000000010101001, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 85, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11101100; b=8'b10000101; op_code=2'b01; // Expected: out=0000000010000100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 86, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10101100; b=8'b11000010; op_code=2'b11; // Expected: out=1000001001011000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 87, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00101001; b=8'b00011010; op_code=2'b10; // Expected: out=0000000000110011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 88, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00100011; b=8'b00010100; op_code=2'b01; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 89, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00001010; b=8'b01111010; op_code=2'b00; // Expected: out=0000000010000100, c_out=0, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 90, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01101111; b=8'b10000011; op_code=2'b01; // Expected: out=0000000000000011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 91, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00111010; b=8'b01010011; op_code=2'b00; // Expected: out=0000000010001101, c_out=0, overflow=1
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 92, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10011111; b=8'b11000000; op_code=2'b01; // Expected: out=0000000010000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 93, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01111100; b=8'b10011010; op_code=2'b00; // Expected: out=0000000000010110, c_out=1, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 94, a, b, op_code, out, c_out, overflow);

    #100 a=8'b00010101; b=8'b11011011; op_code=2'b00; // Expected: out=0000000011110000, c_out=0, overflow=0
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 95, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10101110; b=8'bxxxxxxxx; op_code=2'b11; // Expected: out=0000000000000000, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 96, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10111001; b=8'b11101011; op_code=2'b11; // Expected: out=1010100111010011, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 97, a, b, op_code, out, c_out, overflow);

    #100 a=8'b10001010; b=8'b11110111; op_code=2'b10; // Expected: out=0000000001111101, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 98, a, b, op_code, out, c_out, overflow);

    #100 a=8'b01111101; b=8'b00101100; op_code=2'b11; // Expected: out=0001010101111100, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 99, a, b, op_code, out, c_out, overflow);

    #100 a=8'b11101101; b=8'b11000010; op_code=2'b11; // Expected: out=1011001110011010, c_out=-, overflow=-
    $fwrite(fout, "Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\n", 100, a, b, op_code, out, c_out, overflow);

    $fwrite(fout, "=======================\nAll tests applied.\n");
    $fclose(fout); $stop;
  end
endmodule
