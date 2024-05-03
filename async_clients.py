import asyncio
import socket

IP = '127.0.0.1'
PORT = 12000


async def run_client(client_id):
    reader, writer = await asyncio.open_connection(IP, PORT)
    message = f"Hello from client {client_id}"
    writer.write(message.encode())
    await writer.drain()
    data = await reader.read(1024)
    print(f"Client {client_id}: Received from server: {data.decode()}")
    writer.close()
    await writer.wait_closed()

async def main():
    tasks = [run_client(i) for i in range(100)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

