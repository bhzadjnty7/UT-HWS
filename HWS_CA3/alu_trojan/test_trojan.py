# File: generate_alu_testbench.py
# Purpose: Automatically generate a Verilog testbench ("alu_auto_test.v") that:
#   1) applies multiple test vectors (a, b, op_code) spaced by 100 ns (#100),
#   2) computes expected outputs based on golden full-adder logic,
#   3) writes real outputs to "alu_test_results.txt",
#   4) supports 'x' for invalid a, b, or op_code.


def compute_full_adder_1bit(a_bit, b_bit, c_in):
    """
    Golden full-adder logic for one bit:
      s     = a ^ b ^ c_in
      c_out = ((a ^ b) & c_in) ^ (a & b)
    a_bit, b_bit, c_in each 0 or 1.
    Returns (sum_bit, carry_out_bit).
    """
    s = (a_bit ^ b_bit ^ c_in) & 0x1
    c_out = (((a_bit ^ b_bit) & c_in) ^ (a_bit & b_bit)) & 0x1
    return s, c_out


def compute_expected(a, b, op_code):
    """
    Given a (8-bit int or fallback 0), b (8-bit int or fallback 0), and op_code (0-3 or fallback 0),
    compute golden expected outputs:
      - out16: 16-bit binary string
      - c_out: '0' or '1' or '-'
      - overflow: '0' or '1' or '-'
    """
    # Default
    out16 = 0
    c_out = '-'
    overflow = '-'
    if isinstance(op_code, int) and op_code == 0:
        c_in = 0
        result = 0
        for i in range(8):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            s_bit, c_out = compute_full_adder_1bit(ai, bi, c_in)
            result |= (s_bit << i)
            c_in = c_out
        c_out = c_in
        # signed overflow
        msb_a = (a >> 7) & 1
        msb_b = (b >> 7) & 1
        msb_r = (result >> 7) & 1
        overflow = 1 if (msb_a == msb_b and msb_r != msb_a) else 0
        out16 = result
    elif isinstance(op_code, int) and op_code == 1:
        out16 = a & b
    elif isinstance(op_code, int) and op_code == 3:
        out16 = (a * b) & 0xFFFF
    elif isinstance(op_code, int) and op_code == 2:
        out16 = a ^ b
    # format
    return {'out16': f"{out16:016b}", 'c_out': str(c_out), 'overflow': str(overflow)}


def generate_testbench(filename="alu_auto_test_trojan.v"):
    """
    Generate Verilog testbench:
      - Instantiates alu module
      - Applies test_vectors spaced #100
      - Writes results into alu_test_results.txt
      - Supports 'x' for a, b, or op_code
    """
    test_vectors = [
        (0, 255, 0), (1, 254, 0), (2, 253, 0), (128, 128, 0),
        (127, 1, 0), (100, 50, 0), (255, 255, 0),
        (170, 204, 1), (255, 0, 1), (15, 240, 1),
        (255, 254, 3), (255, 255, 3), (10, 20, 3),
        (15, 15, 3), ('x', 15, 3), (15, 'x', 3),
        (128, 2, 3), (170, 85, 2), (255, 255, 2),
        (5, 10, 2), (0, 0, 'x'), (255, 255, 'x'), (5, 1, 'x'),
    ]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("`timescale 1ns / 1ps\n\nmodule alu_auto_test_trojan;\n")
        f.write("  reg [7:0] a;\n  reg [7:0] b;\n  reg [1:0] op_code;\n")
        f.write("  wire [15:0] out;\n  wire overflow;\n  wire c_out;\n")
        f.write("  alu uut(.a(a), .b(b), .op_code(op_code), .out(out), .overflow(overflow), .c_out(c_out));\n")
        f.write("  integer fout;\n  initial begin\n")
        f.write("    fout = $fopen(\"alu_test_results_trojan.txt\", \"w\");\n")
        f.write("    if(fout==0) $finish;\n    $fwrite(fout, \"Results\n=======================\n\");\n")

        for idx, (aval, bval, opc) in enumerate(test_vectors):
            # compute fallback expected
            exp = compute_expected(
                aval if isinstance(aval,int) else 0,
                bval if isinstance(bval,int) else 0,
                opc if isinstance(opc,int) else 0
            )
            # prepare strings
            if isinstance(aval, str): a_str="8'bxxxxxxxx"; exp={'out16':'0000000000000000','c_out':'-','overflow':'-'}
            else: a_str=f"8'b{aval:08b}"; exp=exp
            if isinstance(bval, str): b_str="8'bxxxxxxxx"; exp={'out16':'0000000000000000','c_out':'-','overflow':'-'}
            else: b_str=f"8'b{bval:08b}"; exp=exp
            if isinstance(opc, str): op_str="2'bxx"; exp={'out16':'0000000000000000','c_out':'-','overflow':'-'}
            else: op_str=f"2'b{opc:02b}"; exp=exp
            comment=f"// Expected: out={exp['out16']}, c_out={exp['c_out']}, overflow={exp['overflow']}"
            f.write(f"    #100 a={a_str}; b={b_str}; op_code={op_str}; {comment}\n")
            f.write("    $fwrite(fout, \"Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\\n\", ")
            f.write(f"{idx+1}, a, b, op_code, out, c_out, overflow);\n\n")

        f.write("    $fwrite(fout, \"=======================\\nAll tests applied.\\n\");\n")
        f.write("    $fclose(fout); $stop;\n  end\nendmodule\n")

    print(f"Generated Verilog testbench: {filename}")

if __name__=='__main__':
    generate_testbench()
