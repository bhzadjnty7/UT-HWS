import socket
import hashlib
import time
import logging
import os

# Configure logging
logging.basicConfig(
    filename='replay_attack.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
HOST = '127.0.0.1'
PORT = 65432
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

def perform_replay_attack():
    """Perform a replay attack simulation"""
    print("\033[95m" + "="*70 + "\033[0m")
    print("\033[95m RFID REPLAY ATTACK SIMULATION \033[0m")
    print("\033[95m" + "="*70 + "\033[0m")
    
    # Step 1: Capture legitimate authentication messages
    print("\033[95m[*] Phase 1: Capturing legitimate communication...\033[0m")
    logging.info("Starting Phase 1: Capturing legitimate communication")
    
    # Store captured messages
    captured_m1 = None
    captured_h1 = None
    captured_m2 = None
    captured_h2 = None
    
    try:
        # First connection to capture messages
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
            print(f"\033[95m[*] Connecting to RFID reader at {HOST}:{PORT}...\033[0m")
            s1.connect((HOST, PORT))
            print("\033[95m[+] Connected to RFID reader\033[0m")
            logging.info(f"Connected to RFID reader at {HOST}:{PORT}")
            
            # Receive M1 and H1 from reader
            data = s1.recv(1024).decode()
            captured_m1, captured_h1 = data.split(',')
            print("\033[95m[+] Captured M1, H1 from reader\033[0m")
            print(f"\033[95m    M1: {captured_m1}\033[0m")
            print(f"\033[95m    H1: {captured_h1}\033[0m")
            logging.info(f"Captured M1: {captured_m1}, H1: {captured_h1}")
            
            # Calculate h(PSK)
            h_psk = calculate_hash(PSK)
            
            # Calculate R1 = h(PSK) XOR M1
            r1_hex = xor_strings(h_psk, captured_m1)
            r1 = int(r1_hex, 16)
            
            # Generate R2
            r2 = 12345678  # Fixed value for demonstration
            r2_hex = format(r2, 'x')
            
            # Calculate M2 = h(PSK) XOR R2
            m2 = xor_strings(h_psk, r2_hex)
            
            # Calculate H2 = h(R1 || R2 || PSK || ID)
            h2 = calculate_hash(str(r1) + str(r2) + PSK + PSK)
            
            # Store for replay
            captured_m2 = m2
            captured_h2 = h2
            
            # Send M2, H2 to reader
            print("\033[95m[*] Sending legitimate M2, H2 to reader...\033[0m")
            s1.sendall(f"{m2},{h2}".encode())
            
            # Receive H3 from reader
            h3 = s1.recv(1024).decode()
            print("\033[95m[+] Received H3 from reader\033[0m")
            logging.info(f"Received H3: {h3}")
            
            # Close first connection
            print("\033[95m[*] Closing first connection\033[0m")
            logging.info("Phase 1 completed successfully")
            
        # Wait a bit before attempting the replay attack
        print("\033[95m[*] Waiting 3 seconds before attempting replay attack...\033[0m")
        time.sleep(3)
        
        # Step 2: Perform replay attack
        print("\n\033[95m[*] Phase 2: Performing replay attack...\033[0m")
        logging.info("Starting Phase 2: Performing replay attack")
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
            print(f"\033[95m[*] Connecting to RFID reader at {HOST}:{PORT}...\033[0m")
            s2.connect((HOST, PORT))
            print("\033[95m[+] Connected to RFID reader\033[0m")
            
            # Receive new M1', H1' from reader
            data = s2.recv(1024).decode()
            new_m1, new_h1 = data.split(',')
            print("\033[95m[+] Received new M1', H1' from reader\033[0m")
            print(f"\033[95m    New M1': {new_m1}\033[0m")
            print(f"\033[95m    New H1': {new_h1}\033[0m")
            logging.info(f"Received new M1': {new_m1}, H1': {new_h1}")
            
            # Now replay the captured M2, H2 from the first session
            print("\033[95m[*] REPLAYING captured M2, H2 from previous session...\033[0m")
            print(f"\033[95m    Replaying M2: {captured_m2}\033[0m")
            print(f"\033[95m    Replaying H2: {captured_h2}\033[0m")
            logging.info(f"Replaying M2: {captured_m2}, H2: {captured_h2}")
            
            s2.sendall(f"{captured_m2},{captured_h2}".encode())
            
            # Receive response from reader
            response = s2.recv(1024).decode()
            print(f"\033[95m[+] Received response from reader: {response}\033[0m")
            logging.info(f"Received response: {response}")
            
            # Check if the attack was successful or not
            if response == "Authentication Failed":
                print("\033[92m[✓] Replay attack was DETECTED and PREVENTED!\033[0m")
                print("\033[95m[*] The protocol successfully prevented the replay attack because:\033[0m")
                print("\033[95m    1. The reader generated a new random R1 for this session\033[0m")
                print("\033[95m    2. H2 verification failed as it depends on the current session's R1\033[0m")
                print("\033[95m    3. Replaying old M2,H2 with a new R1 will always fail verification\033[0m")
                logging.info("Replay attack was detected and prevented")
            else:
                print("\033[91m[!] Replay attack was SUCCESSFUL! This indicates a vulnerability.\033[0m")
                logging.warning("Replay attack was successful - protocol vulnerability detected")
    
    except ConnectionRefusedError:
        print("\033[91m[-] Connection refused. Make sure the RFID reader is running.\033[0m")
        logging.error("Connection refused. RFID reader not available.")
    except Exception as e:
        print(f"\033[91m[-] Error during replay attack: {e}\033[0m")
        logging.error(f"Error during replay attack: {e}")

if __name__ == "__main__":
    # Create log file if it doesn't exist
    if not os.path.exists('replay_attack.log'):
        open('replay_attack.log', 'w').close()
    
    perform_replay_attack()