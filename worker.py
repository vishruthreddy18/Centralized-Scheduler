import socket
import sys
import threading
import time


# print('Received', repr(data))

def sendMaster():
    # HOST = '127.0.0.1'  # The server's hostname or IP address
    # PORT = 4000        # The port used by the server
    # PORT = sys.argv[1]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 4000))
        s.listen()

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data)
 


master = threading.Thread(target=sendMaster)
master.start()

# sleeping to wait for master receiving thread to start
time.sleep(10)

HOST, PORT = '127.0.0.1', 5001

# Implement scheduling Algo here
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 5001))
    s.sendall(b'Job Done')


master.join()