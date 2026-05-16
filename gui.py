import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

from modules.case_manager import create_case, init_db
from modules.hash_verifier import generate_hash
from modules.metadata_analyzer import get_metadata
from modules.hash_analyzer import analyze_hash


# ================= INITIALIZE DATABASE =================
init_db()


# ================= ROOT WINDOW =================
root = tk.Tk()
root.title("DEAK WER Forensic Toolkit")
root.geometry("1000x650")
root.configure(bg="#0a192f")  #dark

# Center window
root.update_idletasks()
width = 1000
height = 650
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# ================= LAYOUT =================

main_area = tk.Frame(root, bg="#0a192f")
main_area.pack(expand=True, fill="both")

# Terminal style header
terminal_label = tk.Label(
    main_area,
    text="> SYSTEM INITIALIZED | FORENSIC ENGINE ACTIVE",
    font=("Consolas", 10),
    fg="#00ff88",
    bg="#0a192f"
)
terminal_label.pack(pady=5)

# ===== BLINK ANIMATION =====
def blink():
    current = terminal_label.cget("fg")
    terminal_label.config(
        fg="#00ff88" if current == "#00ffaa" else "#00ffaa"
    )
    root.after(500, blink)

# Main Title
title_label = tk.Label(
    main_area,
    text="FORENSIC DASHBOARD",
    font=("Consolas", 26, "bold"),
    fg="#00ffc8",
    bg="#0a192f"
)
title_label.pack(pady=10)

subtitle_label = tk.Label(
    main_area,
    text="Digital Evidence Investigation Toolkit",
    font=("Consolas", 12),
    fg="#cccccc",
    bg="#0a192f"
)
subtitle_label.pack(pady=5)

# BUTTON FRAME
button_frame = tk.Frame(main_area, bg="#0a192f")
button_frame.pack(side="right" , padx=40, pady=30)

# DASHBOARD BUTTON STYLES
        
def dashboard_button(text, command):
    return tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Consolas", 12, "bold"),
        bg="#112240",
        fg="#00ffc8",
        activebackground="#00ffaa",
        activeforeground="black",
        width=22,
        height=2,
        bd=0,
        relief="flat",
        highlightbackground="#00ffc8",
        highlightthickness=1
    )


# ================= SPLASH SCREEN =================
def show_splash():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("500x300")
    splash.configure(bg="#0f2027")
    
    splash.update_idletasks()
    x = (splash.winfo_screenwidth() // 2) - 250
    y = (splash.winfo_screenheight() // 2) - 150
    splash.geometry(f"500x300+{x}+{y}")

    tk.Label(
        splash,
        text="DEAK WER FORENSICS",
        font=("Consolas", 24, "bold"),
        fg="#00ffcc",
        bg="#0f2027"
    ).pack(expand=True)
    
   # close splash after 2 sec 
def close_splash():
       splash.destroy()
       root.deiconify()
       blink()  #blink hoga yha

       splash.after(2000, close_splash)


# ================= FUNCTIONS =================

def create_case_window():
    create_case("New Case", "Investigator")
    case_listbox.insert(tk.END, "New Case")


def analyze_evidence():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    hash_value = generate_hash(file_path)
    metadata = get_metadata(file_path)

    result = f"File: {file_path}\n\nSHA256:\n{hash_value}\n\nMetadata:\n{metadata}"
    messagebox.showinfo("Analysis Result", result)


def analyze_hash_input():
    window = tk.Toplevel(root)
    window.title("Hash Analyzer")
    window.geometry("400x250")
    window.configure(bg="#0f2027")

    tk.Label(window, text="Enter Hash:", bg="#0f2027", fg="#00ffcc").pack(pady=10)

    hash_entry = tk.Entry(window, width=40)
    hash_entry.pack(pady=5)
    
    def check():
        result = analyze_hash(hash_entry.get())
        messagebox.showinfo("Result", result)

    tk.Button(
        window,
        text="Analyze",
        command=check,
        bg="#16222A",
        fg="#00ffcc"
    ).pack(pady=10)


def export_report():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return

    with open(file_path, "w") as f:
        f.write("DEAK WER FORENSIC REPORT\n\n")
        for item in case_listbox.get(0, tk.END):
            f.write(f"{item}\n")

    messagebox.showinfo("Success", "Report Exported Successfully")

# ================= CASE HISTORY PANEL =================
    
case_frame = tk.Frame(main_area, bg="#16222A", bd=2, relief="ridge")
case_frame.pack(side="left" , padx=40, pady=20)
button_frame.pack(side="right" , padx=40, pady=20)

case_label = tk.Label(
    case_frame,
    text="CASE HISTORY",
    font=("Consolas", 12, "bold"),
    fg="#00ffaa",
    bg="#16222A"
)
case_label.pack(pady=5)

case_listbox = tk.Listbox(
    case_frame,
    bg="#0d1b2a",
    fg="#00ffc8",
    font=("Consolas", 11),
    bd=0,
    highlightthickness=0,
    width=30,
    height=8
)
case_listbox.pack(padx=10, pady=10)

case_listbox.insert(tk.END, "Case_001")
case_listbox.insert(tk.END, "Case_002")

# ============ BUTTON CALLS ============
dashboard_button("Create Case", create_case_window).pack(pady=10)
dashboard_button("Analyze Evidence", analyze_evidence).pack(pady=10)
dashboard_button("Analyze Hash", analyze_hash_input).pack(pady=10)
dashboard_button("Export Report", export_report).pack(pady=10)

# ================= MAIN DASHBOARD =================
tk.Label(
    main_area,
    text="FORENSIC DASHBOARD",
    font=("Consolas", 26, "bold"),
    fg="#00ffcc",
    bg="#0f2027"
).pack(pady=40)

tk.Label(
    main_area,
    text="Digital Evidence Investigation Toolkit",
    font=("Consolas", 13),
    fg="#cccccc",
    bg="#0f2027"
).pack(pady=5)


# ================= OPTIONAL LOGO =================
try:
    logo_img = Image.open("images/logo.png")
    logo_img = logo_img.resize((120, 120))
    logo_photo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(main_area, image=logo_photo, bg="#0f2027")
    logo_label.image = logo_photo
    logo_label.pack(pady=20)
except:
    pass


# ================= STYLISH CENTER FOOTER =================

footer_frame = tk.Frame(root, bg="#0f2027")
footer_frame.pack(side="bottom", fill="x", pady=15)

footer_label = tk.Label(
    footer_frame,
    text="🚀 Developed by Rohit Dubey  |  DEAK WER FORENSICS 🚀",
    font=("Consolas", 11, "bold"),
    fg="#00ffcc",
    bg="#0f2027"
)
footer_label.pack()

# Neon Glow Effect Animation
def animate_footer():
    colors = ["#00ffcc", "#00ffaa", "#00e6ff", "#00ff99", "#00ffff"]
    current = footer_label.cget("fg")
    next_color = colors[(colors.index(current) + 1) % len(colors)]
    footer_label.config(fg=next_color)
    root.after(500, animate_footer)
animate_footer()


# ================= RUN =================
root.mainloop()

