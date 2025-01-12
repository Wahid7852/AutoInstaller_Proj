import asyncio
import websockets
import subprocess

def download_software_package(package_name):
    try:
        base_url = "https://github.com/Wahid7852/autoInstaller-backend/raw/main"
        bat_script_url = f"{base_url}/install.bat"
        config_file_url = f"{base_url}/packages.config"

        print("Downloading the installation script...")
        subprocess.run(["curl", "-L", bat_script_url, "-o", "install.bat"], check=True)

        print("Downloading the packages.config file...")
        subprocess.run(["curl", "-L", config_file_url, "-o", "packages.config"], check=True)

        print("Executing the installation script...")
        subprocess.run(["install.bat"], check=True)
        print("Installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during script execution: {e}")

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
