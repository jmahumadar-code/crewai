import socket

host = "127.0.0.1"
port = 11434
try:
    with socket.create_connection((host, port), timeout=10) as sock:
        print("Connected successfully")
except ConnectionRefusedError:
    print("Connection refused")
