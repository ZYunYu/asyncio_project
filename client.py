import socket


IP = '127.0.0.1'
PORT = 12000


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((IP, PORT))
        print("Connected to server. Type 'q', 'quit', or 'exit' to stop.")
        while True:
            data = input("Please enter content: ")
            if data.strip().lower() in ("q", "quit", "exit"):
                print("Bye")
                break
            client.send(data.encode("utf-8"))
            response = client.recv(1024).decode("utf-8")
            print(f"Received from server: {response}")


if __name__ == "__main__":
    run_client()
