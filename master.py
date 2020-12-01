import socket
import sys
import threading
import time

def receiveRequest():
    HOST, PORT = "localhost", 5000


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
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

def sendWorker():

    HOST1 = 'localhost'  # The server's hostname or IP address
    PORT1 = 5001       # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST1, PORT1))
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

receiver = threading.Thread(target=receiveRequest)

receiver.start()


worker = threading.Thread(target=sendWorker)
worker.start()

# sleeping to wait for worker receiving thread to start
time.sleep(10)

val = input("Enter Port Number: ")
HOST, PORT = "localhost", int(val)
# HOST, PORT = "localhost", 4000

# Implement scheduling Algos here

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'job Given')



receiver.join()
worker.join()