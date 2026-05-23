import socket
import json

class ChessServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.running = False
        
    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")
        self.client_socket, addr = self.server_socket.accept()
        self.client_socket.settimeout(5)
        print(f"Client connected from {addr}")
        self.running = True
        
    def send_move(self, move_data):
        """Send move to opponent"""
        try:
            print(f"Sending move: {move_data}")
            message = json.dumps(move_data)
            self.client_socket.sendall(message.encode())
        except Exception as e:
            print(f"Error sending move: {e}")
            self.running = False
            
    def receive_move(self):
        """Receive move from opponent"""
        try:
            message = self.client_socket.recv(1024).decode()
            if message:
                return json.loads(message)
        except socket.timeout:
            return None
        except Exception as e:
            print(f"Error receiving move: {e}")
            self.running = False
        return None
        
    def close(self):
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()

class ChessClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)
        self.socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")
        self.running = True
        
    def send_move(self, move_data):
        """Send move to opponent"""
        try:
            message = json.dumps(move_data)
            self.socket.sendall(message.encode())
        except Exception as e:
            print(f"Error sending move: {e}")
            self.running = False

    def receive_move(self):
        """Receive move from opponent"""
        try:
            message = self.socket.recv(1024).decode()
            print(f"Received move: {message}")
            if message:
                return json.loads(message)
        except socket.timeout:
            return None
        except Exception as e:
            print(f"Error receiving move: {e}")
            self.running = False
        return None
        
    def close(self):
        if self.socket:
            self.socket.close()
        self.running = False