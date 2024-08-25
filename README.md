**Software Installation Automation**

- Project Introduction
The Software Installation Automation project is a Python-based desktop application designed to streamline the process of installing software packages across multiple computers in IT and CS labs. With a user-friendly interface and seamless communication via WebSockets, this tool enables administrators to install necessary software packages remotely, ensuring that all lab machines are updated and configured consistently.
Target Audience

**This project is specifically directed towards:**

- System Administrators: Manage and automate the software installation process across multiple lab computers.
- Educational Institutions: Ensure that lab computers are uniformly set up with the required software packages for various semesters.
- IT Professionals: Simplify the deployment of software packages in environments where manual installation is impractical.

**Key Features**

- Lab-Specific Software Deployment: Choose between IT Lab and CS Lab, each containing predefined groups of IP addresses for the machines in those labs.
- Semester-Based Software Packages: Select from Semester 1 to 6, with predefined software packages (VS Code, Python, MySQL).
- Remote Installation: Send installation commands via WebSocket to all machines in the selected lab, ensuring that the required software is installed without the need for physical presence.
- Acknowledgment Check: Includes a mandatory acknowledgment checkbox to prevent accidental installations.
- Update Functionality: Placeholder for future updates to the software deployment process.

**-How to Run**

**Prerequisites**

    Python 3.x: Ensure that Python is installed on your system.

    Required Libraries: Install the necessary Python libraries by running:
    pip install -r requirements.txt

Running the Application

    Clone the Repository:
    git clone https://github.com/yourusername/software-installation-automation.git
    
    cd software-installation-automation

Run the Application:

    Launch the application by executing the following command:
        python LAB_Control.py

        The application window will open, maximized by default, with a clean and intuitive user interface.

Using the Application:
        
1. Select Lab: Choose either "IT Lab" or "CS Lab" from the dropdown list.
2. Software Package: Select the appropriate semester (1 to 6) from the dropdown menu.
3. Acknowledge: Check the acknowledgment box to confirm the software installation.
4. Install: Click the "Install" button to initiate the software installation process.
5. Update: Use the "Update" button to refresh the software installation configuration (feature to be implemented).

**Scope**

This project aims to provide a robust solution for automating software installations across lab environments. The current scope includes:
    
- Basic WebSocket communication: The application sends installation commands to lab machines over a WebSocket connection.
- Predefined Software Packages: The application includes predefined software packages for educational semesters.
- User Interface: A user-friendly and techy interface designed to be intuitive for administrators.

**Future Enhancements:**

- Dynamic Software Selection: Allow administrators to dynamically choose software packages to install.
- Detailed Logs: Implement logging to track installation status and errors.
- Update Feature: Fully develop the update functionality to allow updating software packages remotely.
