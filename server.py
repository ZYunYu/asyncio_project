import socket
import asyncio

IP = '127.0.0.1'
PORT = 12000
BUFFER_SIZE = 1024

async def echo(conn: socket.socket, addr):
    loop = asyncio.get_running_loop()
    try:
        while True:
            data = await loop.sock_recv(conn, BUFFER_SIZE)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Message from {addr}: {message}")
            await loop.sock_sendall(conn, data + b"~")
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        print(f"Connection closed with {addr}")
        conn.close()

async def listen_for_conn(server: socket.socket):
    loop = asyncio.get_running_loop()
    while True:
        conn, addr = await loop.sock_accept(server)
        conn.setblocking(False)
        print(f"Received connection from client {addr}")
        asyncio.create_task(echo(conn, addr))

async def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind((IP, PORT))
    server.listen(5)
    print("Server starts, waiting for connection...")
    await listen_for_conn(server)

# Start the server
asyncio.run(main())

