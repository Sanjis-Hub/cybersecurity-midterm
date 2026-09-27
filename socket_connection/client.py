import socket

HOST = "127.0.0.1"
PORT = 5000


def start_client():
    """Connect to the local server, send a message, and receive a response."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        message = input("Enter a message for the server: ")
        client_socket.sendall(message.encode("utf-8"))

        response = client_socket.recv(1024)

        if response:
            print(f"Server response: {response.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Connection failed: The server is not running.")

    except OSError as error:
        print(f"Client error: {error}")

    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    start_client()
