import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")

def generate_report(file_path, hash_value, metadata):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    report_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    report_path = os.path.join(REPORT_DIR, report_name)

    with open(report_path, "w") as f:
        f.write("DEAK WER FORENSIC REPORT\n")
        f.write("="*40 + "\n")
        f.write(f"Generated On: {datetime.now()}\n\n")
        f.write(f"File: {file_path}\n")
        f.write(f"SHA256: {hash_value}\n\n")
        f.write("Metadata:\n")
        for key, value in metadata.items():
            f.write(f"{key}: {value}\n")

    return report_path
