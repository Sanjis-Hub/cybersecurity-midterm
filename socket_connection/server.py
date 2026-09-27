import socket

HOST = "127.0.0.1"
PORT = 5000


def start_server():
    """Start the TCP server and handle one client connection."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")
        print("Waiting for a client connection...")

        client_socket, client_address = server_socket.accept()
        print(f"Client connected from {client_address}")

        data = client_socket.recv(1024)

        if data:
            message = data.decode("utf-8")
            print(f"Client message: {message}")

            response = "Message received by the server."
            client_socket.sendall(response.encode("utf-8"))

        client_socket.close()
        print("Client connection closed.")

    except OSError as error:
        print(f"Server error: {error}")

    finally:
        server_socket.close()
        print("Server shut down.")


if __name__ == "__main__":
    start_server()
