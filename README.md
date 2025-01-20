# Software Installation Automation

## Project Introduction
The Software Installation Automation project is a Python-based application designed to streamline the software installation process across multiple systems in IT and CS labs. By leveraging WebSocket communication and a user-friendly interface, this tool enables administrators to remotely install, update, and manage software packages efficiently.

## Target Audience

This project is designed for:

- **System Administrators:** Simplify software deployment across multiple lab computers.
- **Educational Institutions:** Maintain uniform software setups for different semesters in IT and CS labs.
- **IT Professionals:** Automate software deployment in large-scale environments, reducing manual effort.

## Key Features

### LabManager
- **Lab-Specific Software Deployment:**
  - Choose between "IT Lab" and "CS Lab," each mapped to predefined groups of IP addresses.
- **Semester-Based Software Selection:**
  - Select semester-specific software packages (e.g., VS Code, Python, MySQL).
- **Git Token Integration:**
  - Prompt administrators to enter their Git token before installation. The token is securely passed to the client PCs for downloading installation files.
- **Remote Installation Commands:**
  - Send commands over WebSocket to execute software installations on remote systems.
- **Acknowledgment Confirmation:**
  - Prevent accidental installations with a mandatory acknowledgment checkbox.

### LabClient
- **WebSocket Server:**
  - Receives commands from Lab_Control to execute installation scripts.
- **Automated Script Execution:**
  - Downloads and runs installation scripts (`install.bat`) and package configurations (`packages.config`) from a GitHub repository.
- **Error Handling and Logs:**
  - Logs errors and execution statuses for monitoring.
- **Integration with Chocolatey:**
  - Uses Chocolatey to install software based on the configuration file.
- Hardcodes GitHub auth token
  
## How to Run

### Prerequisites
- **Python 3.x:** Ensure Python is installed.
- **Required Libraries:**
  Install the necessary dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- **PyInstaller:**
  To create standalone executables:
  ```bash
  pip install pyinstaller
  ```

### Running Lab_Control
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/software-installation-automation.git
   cd software-installation-automation
   ```
2. Start the application:
   ```bash
   python Lab_Control.py
   ```
3. Use the interface to select labs, software packages, and initiate installation.

### Running Lab_pc
1. Use PyInstaller to create a standalone `.exe` for Lab_pc:
   ```bash
   pyinstaller --onefile --noconsole Lab_pc.py
   ```
2. Copy the `.exe` to the target machine.
3. Run the `.exe` to start the WebSocket server.

## Workflow
1. **Lab_Control:**
   - Prompts the user for a Git token.
   - Sends installation commands along with the token to client PCs via WebSocket.
2. **Lab_pc:**
   - Downloads `install.bat` and `packages.config` using the Git token.
   - Executes the `install.bat` to install the required software using Chocolatey.

## Scope
The project provides a reliable solution for automating software installations in lab environments. It includes:
- WebSocket communication for remote command execution.
- Predefined software packages tailored for educational purposes.
- Git token-based authentication for secure file downloads.

## Future Enhancements
- **Dynamic Software Selection:**
  - Enable administrators to define software packages dynamically.
- **Detailed Logs:**
  - Implement a logging mechanism to track installation progress and errors.
- **Live Monitoring:**
  - Add a real-time dashboard to monitor installation status across systems.
- **Enhanced Update Functionality:**
  - Develop a feature to update existing installations remotely.
