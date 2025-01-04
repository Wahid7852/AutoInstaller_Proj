import asyncio
import websockets
import subprocess

async def ws_server(websocket, path):
    print("WebSocket server started.")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            if message.startswith("download:"):
                software_name = message.split(":", 1)[1]
                download_software(software_name)
    except websockets.ConnectionClosedError:
        print("Connection closed.")

def download_software(software_name):
    try:
        software_url = f"https://github.com/YourUsername/YourRepo/raw/main/softwares/{software_name}.exe"
        subprocess.run(["curl", "-L", software_url, "-o", f"{software_name}.exe"], check=True)
        print(f"{software_name} downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {software_name}: {e}")

async def start_ws_server():
    server = await websockets.serve(ws_server, "0.0.0.0", 35369)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_ws_server())
