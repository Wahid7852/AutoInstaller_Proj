import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import asyncio
import websockets
from PIL import Image, ImageTk

ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

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

SEMESTER_SOFTWARES = {
    "Semester 1": ["VS Code", "Turbo C", "MySQL Workbench", "Python", "XAAMP", "Scilab", "Cisco Packet Tracer"],
    "Semester 2": ["Java", "VS Code", "Turbo C", "MySQL Workbench", "Python", "XAAMP", "Scilab"],
    "Semester 3": ["Java", "Oracle (PL/SQL)", "Turbo C", "VS Code", "Python", "XAAMP", "MYSQL", "Flutter"],
    "Semester 4": ["VS Code", "Turbo C", "MySQL Workbench", "Python", "Netbeans", "Java", "Oracle"],
    "Semester 5": ["VS Code", "Turbo C", "MySQL Workbench", "Python", "Netbeans", "Java", "Oracle", "Selenium", "StarUML"],
    "Semester 6": ["Python", "Netbeans", "Java", "Oracle", "Selenium", "StarUML", "MongoDB", "R Studio"]
}

async def send_request(ip_address, command):
    uri = f"ws://{ip_address}:35369"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(command)
            print(f"Sent '{command}' to {ip_address}")
    except asyncio.TimeoutError:
        print(f"Timeout connecting to {ip_address}. Moving to the next IP.")
    except Exception as e:
        print(f"Error connecting to {ip_address}: {e}")

async def send_requests_to_group(ip_group, command):
    for ip_address in ip_group:
        await send_request(ip_address, command)
    await asyncio.sleep(3)

def on_install_button_click():
    selected_lab = lab_combobox.get()
    selected_semester = semester_combobox.get()

    if not selected_lab:
        CTkMessagebox(title="Warning", message="Please select a lab", icon="warning")
        return

    if not selected_semester:
        CTkMessagebox(title="Warning", message="Please select a software package", icon="warning")
        return

    if not acknowledge_var.get():
        CTkMessagebox(title="Warning", message="Please acknowledge", icon="warning")
        return

    command = "open_notepad"
    ip_groups = LAB_IPS[selected_lab]
    for ip_group in ip_groups:
        asyncio.run(send_requests_to_group(ip_group, command))
    CTkMessagebox(title="Info", message="Requests sent successfully", icon="info")

def on_update_button_click():
    CTkMessagebox(title="Update", message="Update functionality is not implemented yet.", icon="info")

def on_list_softwares_button_click():
    selected_semester = semester_combobox.get()
    if not selected_semester:
        CTkMessagebox(title="Warning", message="Please select a software package", icon="warning")
        return

    software_list = SEMESTER_SOFTWARES.get(selected_semester, [])
    software_display = "\n".join(software_list) if software_list else "No software available for this semester."
    CTkMessagebox(title="Software List", message=f"List of software packages for {selected_semester}:\n\n{software_display}", icon="info")

root = ctk.CTk()
root.title("Automated Software Installer")
root.geometry("800x600")

# Load and set the background image
bg_image = Image.open("images/tech_background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = ctk.CTkLabel(root, image=bg_photo, text="")
background_label.place(relwidth=1, relheight=1)

# Transparent center frame
center_frame = ctk.CTkFrame(root, corner_radius=10, fg_color="transparent")
center_frame.pack(pady=20, padx=20, fill="both", expand=True)

font_large = ctk.CTkFont(size=18, weight="bold")
font_medium = ctk.CTkFont(size=14)

lab_label = ctk.CTkLabel(center_frame, text="Select Lab", font=font_large)
lab_label.pack(pady=10)

lab_combobox = ctk.CTkComboBox(center_frame, values=list(LAB_IPS.keys()), width=300)
lab_combobox.pack(pady=10)

semester_label = ctk.CTkLabel(center_frame, text="Software Package:", font=font_large)
semester_label.pack(pady=10)

semesters = [f"Semester {i}" for i in range(1, 7)]
semester_combobox = ctk.CTkComboBox(center_frame, values=semesters, width=300)
semester_combobox.pack(pady=10)

acknowledge_var = ctk.BooleanVar()
acknowledge_checkbutton = ctk.CTkCheckBox(
    center_frame, 
    text="I acknowledge the above software will be installed", 
    variable=acknowledge_var,
    font=font_medium
)
acknowledge_checkbutton.pack(pady=10)

buttons_frame = ctk.CTkFrame(center_frame, fg_color="transparent")
buttons_frame.pack(pady=20)

install_button = ctk.CTkButton(buttons_frame, text="Install", command=on_install_button_click, font=font_large)
install_button.pack(side="left", padx=10)

update_button = ctk.CTkButton(buttons_frame, text="Update", command=on_update_button_click, font=font_large)
update_button.pack(side="left", padx=10)

list_softwares_button = ctk.CTkButton(buttons_frame, text="List Softwares", command=on_list_softwares_button_click, font=font_large)
list_softwares_button.pack(side="left", padx=10)

root.mainloop()
