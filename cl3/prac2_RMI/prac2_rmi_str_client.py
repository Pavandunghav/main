import Pyro5.api

def main():
    # Paste the URI from the server here
    uri = input("Enter server URI (e.g., PYRO:obj_123456@localhost:port): ")
    string_service = Pyro5.api.Proxy(uri)

    # Input strings from user
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # Remote call
    result = string_service.concatenate(str1, str2)
    print("Concatenated result:", result)

if __name__ == "__main__":
    main()
