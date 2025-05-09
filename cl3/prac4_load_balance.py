import threading
import time
import random
from queue import Queue

# Simulated Server class
class Server:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

    def handle_request(self, request_id):
        with self.lock:
            print(f"Server {self.name} is processing Request {request_id}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate processing time
            print(f"Server {self.name} finished Request {request_id}")

# Load Balancer using Round Robin
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0
        self.lock = threading.Lock()

    def get_next_server(self):
        with self.lock:
            server = self.servers[self.index]
            self.index = (self.index + 1) % len(self.servers)
            return server

    def handle_request(self, request_id):
        server = self.get_next_server()
        threading.Thread(target=server.handle_request, args=(request_id,)).start()

# Simulate client requests
def simulate_clients(load_balancer, total_requests=10):
    for i in range(1, total_requests + 1):
        print(f"Client sending Request {i}")
        load_balancer.handle_request(i)
        time.sleep(random.uniform(0.2, 0.5))  # Simulate time between client requests

# Main Execution
if __name__ == "__main__":
    # Create servers
    servers = [Server(f"S{i}") for i in range(1, 4)]

    # Create Load Balancer
    lb = LoadBalancer(servers)

    # Simulate Clients
    simulate_clients(lb, total_requests=15)

