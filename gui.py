import tkinter as tk
from tkinter import messagebox, filedialog
from modules.case_manager import create_case, init_db
from modules.hash_verifier import generate_hash
from modules.metadata_analyzer import get_metadata
from modules.hash_analyzer import analyze_hash

init_db()

root = tk.Tk()
root.title("DEAK WER Forensic Toolkit")
root.geometry("400x350")

tk.Label(root, text="DEAK WER Forensic Toolkit", font=("Arial", 16)).pack(pady=20)

# ---------- CREATE CASE ----------
def create_case_window():
    window = tk.Toplevel(root)
    window.title("Create Case")

    tk.Label(window, text="Case Name").pack()
    case_entry = tk.Entry(window)
    case_entry.pack()

    tk.Label(window, text="Investigator Name").pack()
    inv_entry = tk.Entry(window)
    inv_entry.pack()

    def save_case():
        create_case(case_entry.get(), inv_entry.get())
        messagebox.showinfo("Success", "Case Created!")
        window.destroy()

    tk.Button(window, text="Save Case", command=save_case).pack(pady=10)

# ---------- ANALYZE EVIDENCE ----------
def analyze_evidence():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    hash_value = generate_hash(file_path)
    metadata = get_metadata(file_path)

    result = f"File: {file_path}\nSHA256: {hash_value}\nMetadata:\n{metadata}"
    messagebox.showinfo("Analysis Result", result)

# ---------- HASH INPUT ANALYZER -----------
def analyze_hash_input():
    hash_value = hash_entry.get().strip()

    if not hash_value:
        messagebox.showwarning("Input Error", "No hash value entered!")
        return

    if len(hash_value) not in [32, 40, 64]:
        messagebox.showwarning("Invalid Hash", "Hash length looks incorrect.")
        return

    result = analyze_hash(hash_value)
    messagebox.showinfo("Hash Analysis Result", result)

# --------- HASH ANALYZER UI ------------
tk.Label(root, text="Analyze Hash Value", font=("Arial", 12)).pack(pady=5)

hash_entry = tk.Entry(root, width=40)
hash_entry.pack(pady=5)

tk.Button(root, text="Analyze Hash", width=25, command=analyze_hash_input).pack(pady=5)

# ---------- BUTTONS ----------
tk.Button(root, text="Create New Case", width=25, command=create_case_window).pack(pady=10)
tk.Button(root, text="Analyze Evidence", width=25, command=analyze_evidence).pack(pady=10)

root.mainloop()

