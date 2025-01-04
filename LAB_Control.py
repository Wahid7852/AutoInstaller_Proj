import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import asyncio
import websockets
import json

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

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

LOCAL_SOFTWARE_JSON = "software_list.json"

async def send_request(ip_address, command):
    uri = f"ws://{ip_address}:35369"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(command)
    except (asyncio.TimeoutError, Exception):
        pass

async def send_requests_to_group(ip_group, command):
    tasks = [send_request(ip, command) for ip in ip_group]
    await asyncio.gather(*tasks)
    await asyncio.sleep(3)

def fetch_software_list():
    try:
        with open(LOCAL_SOFTWARE_JSON, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        CTkMessagebox(title="Error", message=f"Failed to load software list: {e}", icon="error")
        return {}

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

    software_list = fetch_software_list()
    semester_softwares = software_list.get(selected_semester, [])
    for software in semester_softwares:
        command = f"download:{software}"
        ip_groups = LAB_IPS[selected_lab]
        for ip_group in ip_groups:
            asyncio.run(send_requests_to_group(ip_group, command))
    CTkMessagebox(title="Info", message="Download requests sent successfully", icon="info")

def on_update_button_click():
    CTkMessagebox(title="Update", message="Update functionality is not implemented yet.", icon="info")

def on_list_softwares_button_click():
    software_list = fetch_software_list()
    selected_semester = semester_combobox.get()

    if not selected_semester:
        CTkMessagebox(title="Warning", message="Please select a software package", icon="warning")
        return

    semester_softwares = software_list.get(selected_semester, [])
    if not semester_softwares:
        CTkMessagebox(title="Info", message="No software available for this semester.", icon="info")
        return

    software_display = "\\n".join(semester_softwares)
    CTkMessagebox(title="Software List", message=f"List of software packages for {selected_semester}:\\n\\n{software_display}", icon="info")

root = ctk.CTk()
root.title("Automated Software Installer")
root.geometry("800x600")

center_frame = ctk.CTkFrame(root, corner_radius=10, fg_color="transparent")
center_frame.pack(pady=20, padx=20, fill="both", expand=True)

font_large = ctk.CTkFont(size=18, weight="bold")
font_medium = ctk.CTkFont(size=14)

lab_label = ctk.CTkLabel(center_frame, text="Select Lab", font=font_large)
lab_label.pack(pady=10)

lab_combobox = ctk.CTkComboBox(center_frame, values=list(LAB_IPS.keys()), width=300, state="readonly")
lab_combobox.pack(pady=10)

semester_label = ctk.CTkLabel(center_frame, text="Software Package:", font=font_large)
semester_label.pack(pady=10)

software_list = fetch_software_list()
semesters = list(software_list.keys())
semester_combobox = ctk.CTkComboBox(center_frame, values=semesters, width=300, state="readonly")
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
