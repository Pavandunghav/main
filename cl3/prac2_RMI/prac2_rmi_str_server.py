
import Pyro5.api

@Pyro5.api.expose
class StringConcatenator:
    def concatenate(self, str1, str2):
        return str1 + str2

def main():
    daemon = Pyro5.server.Daemon()                     # Start a Pyro server
    uri = daemon.register(StringConcatenator)          # Register the class as a Pyro object
    print("Server is ready. URI:", uri)
    daemon.requestLoop()                               # Start the event loop of the server

if __name__ == "__main__":
    main()
