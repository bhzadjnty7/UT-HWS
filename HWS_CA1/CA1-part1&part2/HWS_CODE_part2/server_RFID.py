import socket
import hashlib
import random
import logging
import time
import os

# Configure logging
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
HOST = '127.0.0.1'
PORT = 65432
PSK = "810103098"  # Pre-shared key (student ID)

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

def start_server():
    """Start the RFID reader server"""
    print("\033[92m[+] RFID reader listening on {}:{}\033[0m".format(HOST, PORT))
    logging.info("RFID reader started")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        while True:
            print("\033[92m[*] Waiting for RFID tag connection...\033[0m")
            conn, addr = s.accept()
            with conn:
                print(f"\033[92m[+] RFID tag connected from {addr}\033[0m")
                logging.info(f"RFID tag connected from {addr}")
                
                try:
                    # Step 1: Generate R1
                    R1 = generate_random_number()
                    print(f"\033[92m[*] Generated random number R1: {R1}\033[0m")
                    logging.info(f"Generated random number R1: {R1}")
                    
                    # Calculate h(PSK)
                    h_psk = calculate_hash(PSK)
                    logging.info(f"h(PSK): {h_psk}")
                    
                    # Calculate M1 = h(PSK) XOR R1
                    R1_hex = format(R1, 'x')
                    M1 = xor_strings(h_psk, R1_hex)
                    logging.info(f"M1 = h(PSK) XOR R1: {M1}")
                    
                    # Calculate H1 = h(R1 || PSK)
                    H1 = calculate_hash(str(R1) + PSK)
                    logging.info(f"H1 = h(R1 || PSK): {H1}")
                    
                    # Step 2: Send M1 and H1 to tag
                    print("\033[92m[*] Sending authentication challenge to tag...\033[0m")
                    conn.sendall(f"{M1},{H1}".encode())
                    
                    # Step 5: Receive M2 and H2 from tag
                    print("\033[92m[*] Waiting for tag response...\033[0m")
                    data = conn.recv(1024).decode()
                    if not data:
                        print("\033[91m[-] No response received from tag\033[0m")
                        logging.error("No response received from tag")
                        continue
                    
                    M2, H2 = data.split(',')
                    logging.info(f"Received M2: {M2}, H2: {H2}")
                    print("\033[92m[+] Received response from tag\033[0m")
                    
                    # Step 6: Calculate R2 = h(PSK) XOR M2
                    R2_hex = xor_strings(h_psk, M2)
                    # Convert R2 from hex to int for further processing
                    try:
                        R2 = int(R2_hex, 16)
                        logging.info(f"Calculated R2: {R2}")
                        
                        # Verify H2 = h(R1 || R2 || PSK || ID)
                        # In this case, ID is the same as PSK for simplicity
                        H2_calculated = calculate_hash(str(R1) + str(R2) + PSK + PSK)
                        logging.info(f"Calculated H2: {H2_calculated}")
                        
                        if H2 == H2_calculated:
                            print("\033[92m[+] Tag authenticated successfully!\033[0m")
                            logging.info("Tag authenticated successfully")
                            
                            # Step 7: Calculate H3 = h(R2 || PSK)
                            H3 = calculate_hash(str(R2) + PSK)
                            logging.info(f"H3 = h(R2 || PSK): {H3}")
                            
                            # Step 8: Send H3 to tag
                            print("\033[92m[*] Sending confirmation to tag...\033[0m")
                            conn.sendall(H3.encode())
                            print("\033[92m[+] Mutual authentication completed successfully!\033[0m")
                            logging.info("Mutual authentication completed")
                        else:
                            print("\033[91m[-] Tag authentication failed! H2 mismatch\033[0m")
                            logging.error("Tag authentication failed: H2 mismatch")
                            conn.sendall("Authentication Failed".encode())
                    except ValueError:
                        print("\033[91m[-] Invalid R2 value received\033[0m")
                        logging.error("Invalid R2 value received")
                        conn.sendall("Authentication Failed".encode())
                        
                except Exception as e:
                    print(f"\033[91m[-] Error during authentication: {e}\033[0m")
                    logging.error(f"Error during authentication: {e}")
                    conn.sendall("Authentication Failed".encode())

if __name__ == "__main__":
    # Create log file if it doesn't exist
    if not os.path.exists('server.log'):
        open('server.log', 'w').close()
    
    start_server()