import asyncio
import websockets
import subprocess

async def ws_server(websocket, path):
    print("WebSocket server started.")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            if message == "open_notepad":
                subprocess.Popen(["notepad.exe"])  
    except websockets.ConnectionClosedError:
        print("Connection closed.")

async def start_ws_server():
    server = await websockets.serve(ws_server, "0.0.0.0", 35369)
    await server.wait_closed()

async def main():
    await start_ws_server()

if __name__ == "__main__":
    asyncio.run(main())
