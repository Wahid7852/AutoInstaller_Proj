import asyncio
import websockets
import subprocess

def download_software_package(package_name):
    try:
        zip_url = f"https://github.com/YourUsername/YourRepo/raw/main/packages/{package_name}.zip"
        subprocess.run(["curl", "-L", zip_url, "-o", f"{package_name}.zip"], check=True)
        print(f"{package_name} package downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {package_name} package: {e}")

async def ws_server(websocket, path):
    print("WebSocket server started.")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            if message.startswith("download:"):
                package_name = message.split(":", 1)[1]
                download_software_package(package_name)
    except websockets.ConnectionClosedError:
        print("Connection closed.")

async def start_ws_server():
    server = await websockets.serve(ws_server, "0.0.0.0", 35369)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_ws_server())
