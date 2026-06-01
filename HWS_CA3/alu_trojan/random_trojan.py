import sys, os
# Safely import the standard library random even if this file is named random.py
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir in sys.path:
    sys.path.remove(script_dir)
import random as rnd
# Restore path
sys.path.insert(0, script_dir)
# Seed for reproducibility
rnd.seed(42)


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
    Given a (0–255), b (0–255), op_code (0–3), compute expected golden outputs:
      - out16: 16-bit binary string
      - c_out: '0' or '1' or '-' if not ADD
      - overflow: '0' or '1' or '-' if not ADD
    """
    out16 = 0
    c_out = '-'
    overflow = '-'
    if op_code == 0:
        c_in = 0
        result = 0
        for i in range(8):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            s_bit, c_in = compute_full_adder_1bit(ai, bi, c_in)
            result |= (s_bit << i)
        c_out = c_in
        msb_a = (a >> 7) & 1
        msb_b = (b >> 7) & 1
        msb_r = (result >> 7) & 1
        overflow = 1 if (msb_a == msb_b and msb_r != msb_a) else 0
        out16 = result
    elif op_code == 1:
        out16 = a & b
    elif op_code == 2:
        out16 = a ^ b
    elif op_code == 3:
        out16 = (a * b) & 0xFFFF
    return {'out16': f"{out16:016b}", 'c_out': str(c_out), 'overflow': str(overflow)}


def generate_testbenchRANDOM(filename="alu_auto_test_trojan_random.v", num_tests=100):
    """
    Generate Verilog testbench with num_tests random vectors:
      - a, b ∈ [0,255] or 'x' (5% chance each)
      - op_code ∈ {0,1,2,3} or 'x' (5% chance)
      - spaced by #100 ns
      - writes results to alu_test_resultsRANDOM.txt
    """
    test_vectors = []
    for _ in range(num_tests):
        def rand_field(width):
            return 'x' if rnd.random() < 0.05 else rnd.randint(0, (1<<width)-1)
        a_val = rand_field(8)
        b_val = rand_field(8)
        op_val = 'x' if rnd.random() < 0.05 else rnd.randint(0,3)
        test_vectors.append((a_val, b_val, op_val))

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("`timescale 1ns / 1ps\n\nmodule alu_auto_test_trojan_random;\n")
        f.write("  reg [7:0] a;\n  reg [7:0] b;\n  reg [1:0] op_code;\n")
        f.write("  wire [15:0] out;\n  wire overflow;\n  wire c_out;\n")
        f.write("  alu uut(.a(a), .b(b), .op_code(op_code), .out(out), .overflow(overflow), .c_out(c_out));\n")
        f.write("  integer fout;\n  initial begin\n")
        f.write("    fout = $fopen(\"alu_test_results_trojan_random.txt\", \"w\");\n")
        f.write("    if (fout==0) $finish;\n    $fwrite(fout, \"Results\n=======================\n\");\n")

        for idx, (aval, bval, opc) in enumerate(test_vectors):
            a_num = aval if isinstance(aval,int) else 0
            b_num = bval if isinstance(bval,int) else 0
            op_num = opc if isinstance(opc,int) else 0
            exp = compute_expected(a_num, b_num, op_num)

            a_str = "8'bxxxxxxxx" if isinstance(aval,str) else f"8'b{aval:08b}"
            b_str = "8'bxxxxxxxx" if isinstance(bval,str) else f"8'b{bval:08b}"
            op_str= "2'bxx" if isinstance(opc,str) else f"2'b{opc:02b}"

            if isinstance(aval,str) or isinstance(bval,str) or isinstance(opc,str):
                exp = {'out16':'0000000000000000','c_out':'-','overflow':'-'}

            comment = f"// Expected: out={exp['out16']}, c_out={exp['c_out']}, overflow={exp['overflow']}"
            f.write(f"    #100 a={a_str}; b={b_str}; op_code={op_str}; {comment}\n")
            f.write("    $fwrite(fout, \"Test %0d: a=%b, b=%b, op=%b => out=%b, c_out=%b, overflow=%b\\n\", ")
            f.write(f"{idx+1}, a, b, op_code, out, c_out, overflow);\n\n")

        f.write("    $fwrite(fout, \"=======================\\nAll tests applied.\\n\");\n")
        f.write("    $fclose(fout); $stop;\n  end\nendmodule\n")

    print(f"Generated Verilog testbench: {filename} with {num_tests} random vectors")

if __name__=='__main__':
    generate_testbenchRANDOM()
