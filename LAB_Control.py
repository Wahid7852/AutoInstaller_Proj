import tkinter as tk
from tkinter import ttk, messagebox
import asyncio
import websockets
from PIL import Image, ImageTk

# Define the IP address groups for the labs
LAB_IPS = {
    'IT Lab': [
        ["192.168.1.10", "192.168.1.11", "192.168.1.12"],
        ["192.168.1.13", "192.168.1.14"],
        ["192.168.1.15"]
    ],
    'CS Lab': [
        ["192.168.2.10", "192.168.2.11", "192.168.2.12"],
        ["192.168.2.13", "192.168.2.14"],
        ["192.168.2.15"]
    ]
}

# Function to send WebSocket request
async def send_request(ip_address, semester):
    uri = f"ws://{ip_address}:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(semester)
        response = await websocket.recv()
        print(response)
        return response

async def send_requests_to_group(ip_group, semester):
    for ip_address in ip_group:
        await send_request(ip_address, semester)

def on_install_button_click():
    selected_lab = lab_combobox.get()
    selected_semester = semester_combobox.get()
    
    if not selected_lab:
        messagebox.showwarning("Warning", "Please select a lab")
        return

    if not selected_semester:
        messagebox.showwarning("Warning", "Please select a semester")
        return

    if not acknowledge_var.get():
        messagebox.showwarning("Warning", "Please acknowledge")
        return

    ip_groups = LAB_IPS[selected_lab]
    for ip_group in ip_groups:
        asyncio.run(send_requests_to_group(ip_group, selected_semester))
    messagebox.showinfo("Info", "Requests sent successfully")

def on_update_button_click():
    # Placeholder function for update functionality
    messagebox.showinfo("Update", "Update functionality is not implemented yet.")

# Create the main application window
root = tk.Tk()
root.title("Automated Software Installer")
root.call("wm", "attributes", ".", "-zoomed", "True")

# Load and set the techy background
bg_image = Image.open("img/tech_background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0)

# Create a frame in the center of the window
center_frame = tk.Frame(root, bg='#2e2e2e')
center_frame.place(relx=0.5, rely=0.5, anchor='center')

# Font settings
font_large = ('Helvetica', 18, 'bold')
font_medium = ('Helvetica', 14)
font_dropdown = ('Helvetica', 16)  # Increased font size for dropdown

# Set the style for the combobox
style = ttk.Style()
style.configure("TCombobox", font=font_dropdown, padding=5)

# Lab selection label and dropdown in one line
lab_frame = tk.Frame(center_frame, bg='#2e2e2e')
lab_frame.pack(pady=10)

lab_label = tk.Label(lab_frame, text="Select Lab", bg='#2e2e2e', fg='#ffffff', font=font_large)
lab_label.pack(side='left', padx=(0, 10))

lab_combobox = ttk.Combobox(lab_frame, values=list(LAB_IPS.keys()), width=30, state='readonly')
lab_combobox.pack(side='left')

# Semester selection label and dropdown
semester_frame = tk.Frame(center_frame, bg='#2e2e2e')
semester_frame.pack(pady=10)

semester_label = tk.Label(semester_frame, text="Software Package:", bg='#2e2e2e', fg='#ffffff', font=font_large)
semester_label.pack(side='left', padx=(0, 10))

# Dropdown for selecting semester
semesters = [f"Semester {i}" for i in range(1, 7)]
semester_combobox = ttk.Combobox(semester_frame, values=semesters, width=30, state='readonly')
semester_combobox.pack(side='left')

# Acknowledgment checkbox
acknowledge_var = tk.BooleanVar()
acknowledge_checkbutton = tk.Checkbutton(
    center_frame,
    text="I acknowledge the above software will be installed",
    variable=acknowledge_var,
    bg='#2e2e2e',
    fg='#ffffff',
    selectcolor='#2e2e2e',
    font=font_medium,
    highlightthickness=0,
    borderwidth=0
)
acknowledge_checkbutton.pack(pady=10)

# Buttons frame
buttons_frame = tk.Frame(center_frame, bg='#2e2e2e')
buttons_frame.pack(pady=20)

# Install button
install_button = tk.Button(buttons_frame, text="Install", command=on_install_button_click, bg='#000000', fg='#ffffff', font=font_large)
install_button.pack(side='left', padx=10)

# Update button
update_button = tk.Button(buttons_frame, text="Update", command=on_update_button_click, bg='#000000', fg='#ffffff', font=font_large)
update_button.pack(side='left', padx=10)

# Allow exit with "Esc" key
root.bind("<Escape>", lambda event: root.destroy())

# Run the application
root.mainloop()
