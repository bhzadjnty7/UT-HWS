import socket
import hashlib
import random
import logging
import time
import os
import sys

# Configure logging
logging.basicConfig(
    filename='client.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
HOST = '127.0.0.1'
PORT = 65432
PSK = "810103098"  # Pre-shared key (student ID)

# For testing wrong PSK scenario
if len(sys.argv) > 1 and sys.argv[1] == "--wrong-psk":
    PSK = "123456789"
    print("\033[93m[!] Using incorrect PSK for testing\033[0m")

def generate_random_number():
    """Generate a random number for authentication"""
    return random.randint(1000000, 9999999)

def calculate_hash(data):
    """Calculate SHA-256 hash of the data"""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()

def xor_strings(str1, str2):
    """XOR two hex strings and return the result as a hex string"""
    # Convert hex strings to integers, XOR them, and convert back to hex string
    result = int(str1, 16) ^ int(str2, 16)
    return format(result, 'x')

def connect_to_reader():
    """Connect to the RFID reader and perform authentication"""
    print("\033[94m[*] RFID tag initializing...\033[0m")
    logging.info("RFID tag initialized")
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"\033[94m[*] Connecting to RFID reader at {HOST}:{PORT}...\033[0m")
            s.connect((HOST, PORT))
            print("\033[94m[+] Connected to RFID reader\033[0m")
            logging.info(f"Connected to RFID reader at {HOST}:{PORT}")
            
            # Step 3: Receive M1 and H1 from reader
            data = s.recv(1024).decode()
            M1, H1 = data.split(',')
            print("\033[94m[+] Received authentication challenge from reader\033[0m")
            logging.info(f"Received M1: {M1}, H1: {H1}")
            
            # Calculate h(PSK)
            h_psk = calculate_hash(PSK)
            logging.info(f"h(PSK): {h_psk}")
            
            # Calculate R1 = h(PSK) XOR M1
            R1_hex = xor_strings(h_psk, M1)
            # Convert R1 from hex to int for further processing
            try:
                R1 = int(R1_hex, 16)
                logging.info(f"Calculated R1: {R1}")
                
                # Verify H1 = h(R1 || PSK)
                H1_calculated = calculate_hash(str(R1) + PSK)
                logging.info(f"Calculated H1: {H1_calculated}")
                
                if H1 == H1_calculated:
                    print("\033[94m[+] Reader challenge verified successfully\033[0m")
                    logging.info("Reader challenge verified successfully")
                    
                    # Step 4: Generate R2
                    R2 = generate_random_number()
                    print(f"\033[94m[*] Generated random number R2: {R2}\033[0m")
                    logging.info(f"Generated random number R2: {R2}")
                    
                    # Calculate M2 = h(PSK) XOR R2
                    R2_hex = format(R2, 'x')
                    M2 = xor_strings(h_psk, R2_hex)
                    logging.info(f"M2 = h(PSK) XOR R2: {M2}")
                    
                    # Calculate H2 = h(R1 || R2 || PSK || ID)
                    # In this case, ID is the same as PSK for simplicity
                    H2 = calculate_hash(str(R1) + str(R2) + PSK + PSK)
                    logging.info(f"H2 = h(R1 || R2 || PSK || ID): {H2}")
                    
                    # Step 5: Send M2 and H2 to reader
                    print("\033[94m[*] Sending response to reader...\033[0m")
                    s.sendall(f"{M2},{H2}".encode())
                    
                    # Step 9: Receive H3 from reader
                    print("\033[94m[*] Waiting for reader confirmation...\033[0m")
                    H3_received = s.recv(1024).decode()
                    
                    if H3_received == "Authentication Failed":
                        print("\033[91m[-] Authentication failed at reader side\033[0m")
                        logging.error("Authentication failed at reader side")
                        return
                    
                    logging.info(f"Received H3: {H3_received}")
                    
                    # Calculate expected H3 = h(R2 || PSK)
                    H3_expected = calculate_hash(str(R2) + PSK)
                    logging.info(f"Expected H3: {H3_expected}")
                    
                    if H3_received == H3_expected:
                        print("\033[94m[+] Reader authenticated successfully!\033[0m")
                        print("\033[94m[+] Mutual authentication completed successfully!\033[0m")
                        logging.info("Reader authenticated successfully")
                        logging.info("Mutual authentication completed")
                    else:
                        print("\033[91m[-] Reader authentication failed! H3 mismatch\033[0m")
                        logging.error("Reader authentication failed: H3 mismatch")
                else:
                    print("\033[91m[-] Reader challenge verification failed! H1 mismatch\033[0m")
                    logging.error("Reader challenge verification failed: H1 mismatch")
            except ValueError:
                print("\033[91m[-] Invalid R1 value received\033[0m")
                logging.error("Invalid R1 value received")
    
    except ConnectionRefusedError:
        print("\033[91m[-] Connection refused. Make sure the RFID reader is running.\033[0m")
        logging.error("Connection refused. RFID reader not available.")
    except Exception as e:
        print(f"\033[91m[-] Error during authentication: {e}\033[0m")
        logging.error(f"Error during authentication: {e}")

if __name__ == "__main__":
    # Create log file if it doesn't exist
    if not os.path.exists('client.log'):
        open('client.log', 'w').close()
    
    connect_to_reader()