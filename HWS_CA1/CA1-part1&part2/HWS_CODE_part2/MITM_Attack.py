import socket
import hashlib
import threading
import time
import logging
import os
import sys

# Configure logging
logging.basicConfig(
    filename='mitm_attack.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
READER_HOST = '127.0.0.1'
READER_PORT = 65432
MITM_HOST = '127.0.0.1'
MITM_PORT = 65433
PSK = "810103098"  # Pre-shared key (student ID)

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

class MITMProxy:
    def __init__(self):
        self.reader_socket = None
        self.tag_socket = None
        self.tag_addr = None
        self.reader_to_tag_thread = None
        self.tag_to_reader_thread = None
        self.attack_performed = False
    
    def start_proxy(self):
        """Start the MITM proxy server"""
        print("\033[96m" + "="*70 + "\033[0m")
        print("\033[96m RFID MAN-IN-THE-MIDDLE ATTACK SIMULATION \033[0m")
        print("\033[96m" + "="*70 + "\033[0m")
        
        print("\033[96m[*] Starting MITM proxy...\033[0m")
        logging.info("Starting MITM proxy")
        
        # Create server socket for tag connections
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((MITM_HOST, MITM_PORT))
        server_socket.listen(1)
        
        print(f"\033[96m[+] MITM proxy listening on {MITM_HOST}:{MITM_PORT}\033[0m")
        print("\033[96m[*] To test MITM attack, run client.py with HOST={MITM_HOST}, PORT={MITM_PORT}\033[0m")
        print("\033[96m[*] You can modify client.py temporarily to connect to the MITM proxy\033[0m")
        print("\033[96m[*] Or you can run: python client.py (after setting environment variables)\033[0m")
        print("\033[96m[*] Example: export RFID_HOST=127.0.0.1 RFID_PORT=65433 && python client.py\033[0m")
        logging.info(f"MITM proxy listening on {MITM_HOST}:{MITM_PORT}")
        
        try:
            # Accept connection from tag
            self.tag_socket, self.tag_addr = server_socket.accept()
            print(f"\033[96m[+] Tag connected from {self.tag_addr}\033[0m")
            logging.info(f"Tag connected from {self.tag_addr}")
            
            # Connect to the real reader
            self.reader_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.reader_socket.connect((READER_HOST, READER_PORT))
            print(f"\033[96m[+] Connected to reader at {READER_HOST}:{READER_PORT}\033[0m")
            logging.info(f"Connected to reader at {READER_HOST}:{READER_PORT}")
            
            # Start threads to handle communication
            self.reader_to_tag_thread = threading.Thread(target=self.reader_to_tag)
            self.tag_to_reader_thread = threading.Thread(target=self.tag_to_reader)
            
            self.reader_to_tag_thread.start()
            self.tag_to_reader_thread.start()
            
            # Wait for threads to finish
            self.reader_to_tag_thread.join()
            self.tag_to_reader_thread.join()
            
            print("\033[96m[*] MITM attack simulation completed\033[0m")
            logging.info("MITM attack simulation completed")
            
        except Exception as e:
            print(f"\033[91m[-] Error in MITM proxy: {e}\033[0m")
            logging.error(f"Error in MITM proxy: {e}")
        finally:
            # Clean up
            if self.reader_socket:
                self.reader_socket.close()
            if self.tag_socket:
                self.tag_socket.close()
            server_socket.close()
    
    def reader_to_tag(self):
        """Handle communication from reader to tag"""
        try:
            # Receive M1, H1 from reader
            data = self.reader_socket.recv(1024).decode()
            if not data:
                return
            
            m1, h1 = data.split(',')
            print("\033[96m[+] Intercepted from reader: M1, H1\033[0m")
            print(f"\033[96m    Original M1: {m1}\033[0m")
            print(f"\033[96m    Original H1: {h1}\033[0m")
            logging.info(f"Intercepted from reader: M1={m1}, H1={h1}")
            
            # Perform MITM attack: Modify M1 (flip some bits)
            modified_m1 = hex(int(m1, 16) ^ 0xFF)[2:]  # XOR with 0xFF to flip bits
            
            print("\033[96m[!] MITM ATTACK: Modifying M1\033[0m")
            print(f"\033[96m    Modified M1: {modified_m1}\033[0m")
            print(f"\033[96m    Original H1: {h1} (unchanged)\033[0m")
            logging.info(f"MITM attack: Modified M1={modified_m1}, H1={h1} (unchanged)")
            
            # Forward modified M1 and original H1 to tag
            self.tag_socket.sendall(f"{modified_m1},{h1}".encode())
            self.attack_performed = True
            
            # Wait for H3 from reader (if authentication succeeds)
            while True:
                data = self.reader_socket.recv(1024).decode()
                if not data:
                    break
                
                print(f"\033[96m[+] Intercepted from reader: {data}\033[0m")
                logging.info(f"Intercepted from reader: {data}")
                
                # Forward to tag
                self.tag_socket.sendall(data.encode())
        
        except Exception as e:
            if "Connection reset by peer" in str(e):
                print("\033[96m[*] Reader closed the connection\033[0m")
                logging.info("Reader closed the connection")
            else:
                print(f"\033[91m[-] Error in reader_to_tag: {e}\033[0m")
                logging.error(f"Error in reader_to_tag: {e}")
    
    def tag_to_reader(self):
        """Handle communication from tag to reader"""
        try:
            # Wait for tag's response (if any)
            try:
                data = self.tag_socket.recv(1024).decode()
                
                # If we get a response from the tag after our attack
                if data and self.attack_performed:
                    print("\033[96m[!] Tag responded despite the MITM attack!\033[0m")
                    print(f"\033[96m    Tag response: {data}\033[0m")
                    logging.info(f"Tag responded despite MITM attack: {data}")
                    
                    # Forward to reader
                    self.reader_socket.sendall(data.encode())
                    
                    # Wait for reader's response
                    reader_response = self.reader_socket.recv(1024).decode()
                    print(f"\033[96m[+] Reader response: {reader_response}\033[0m")
                    logging.info(f"Reader response: {reader_response}")
                    
                    # Forward to tag
                    self.tag_socket.sendall(reader_response.encode())
                else:
                    print("\033[96m[+] No response from tag (connection may have been closed)\033[0m")
                    logging.info("No response from tag (connection may have been closed)")
            except:
                print("\033[96m[✓] Tag rejected the modified message (authentication failed)\033[0m")
                print("\033[96m[+] This demonstrates the protocol's resistance to MITM attacks\033[0m")
                print("\033[96m    The protocol detected the message tampering because:\033[0m")
                print("\033[96m    1. When M1 was modified, the tag calculated an incorrect R1\033[0m")
                print("\033[96m    2. This caused H1 verification to fail (H1 != h(R1||PSK))\033[0m")
                logging.info("Tag rejected the modified message - MITM attack prevented")
        
        except Exception as e:
            if "Connection reset by peer" in str(e):
                print("\033[96m[✓] Tag closed the connection - MITM attack prevented\033[0m")
                logging.info("Tag closed the connection - MITM attack prevented")
            else:
                print(f"\033[91m[-] Error in tag_to_reader: {e}\033[0m")
                logging.error(f"Error in tag_to_reader: {e}")

def check_environment():
    """Check if environment variables are set for the client"""
    if os.environ.get('RFID_HOST') == MITM_HOST and os.environ.get('RFID_PORT') == str(MITM_PORT):
        print("\033[96m[✓] Environment variables are correctly set for the client\033[0m")
    else:
        print("\033[93m[!] Environment variables not set. You may need to modify client.py or set:\033[0m")
        print(f"\033[93m    export RFID_HOST={MITM_HOST} RFID_PORT={MITM_PORT}\033[0m")

if __name__ == "__main__":
    # Create log file if it doesn't exist
    if not os.path.exists('mitm_attack.log'):
        open('mitm_attack.log', 'w').close()
    
    check_environment()
    mitm = MITMProxy()
    mitm.start_proxy()