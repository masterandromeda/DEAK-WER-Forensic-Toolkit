import re
import sqlite3
import hashlib
from datetime import datetime

# ==============================
# 1️⃣ Detect Hash Type
# ==============================
def detect_hash_type(hash_value):
    if re.fullmatch(r"[A-Fa-f0-9]{32}", hash_value):
        return "MD5"
    elif re.fullmatch(r"[A-Fa-f0-9]{40}", hash_value):
        return "SHA1"
    elif re.fullmatch(r"[A-Fa-f0-9]{64}", hash_value):
        return "SHA256"
    else:
        return None


# ==============================
# 2️⃣ Generate SHA256 From File
# ==============================
def generate_sha256(file_path):
    try:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None


# ==============================
# 3️⃣ Save Evidence To Database
# ==============================
def save_evidence_to_db(case_id, file_path, sha256_hash):
    try:
        conn = sqlite3.connect("../database/cases.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO evidence (case_id, file_path, sha256, added_date)
            VALUES (?, ?, ?, ?)
        """, (
            case_id,
            file_path,
            sha256_hash,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()
        return "Saved Successfully"

    except Exception as e:
        return f"DB Error: {e}"


# ==============================
# 4️⃣ Check Duplicate Hash
# ==============================
def check_duplicate(hash_value):
    conn = sqlite3.connect("database/cases.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM evidence WHERE sha256=?", (hash_value,))
    result = cursor.fetchone()

    conn.close()
    return result


# ==============================
# 5️⃣ Main Analyze Function
# ==============================
def analyze_hash(hash_value):

    hash_value = hash_value.strip()

    # ❌ No input
    if not hash_value:
        return "❌ ERROR: No data provided."

    # ❌ Invalid format
    hash_type = detect_hash_type(hash_value)
    if not hash_type:
        return "❌ ERROR: Invalid hash format."

    # 🔍 Duplicate check
    duplicate = check_duplicate(hash_value)

    if duplicate:
        reputation = "Already exists in database"
        risk = "Medium"
        db_status = "Not saved (Duplicate)"
    else:
        reputation = "New Evidence"
        risk = "Low"

        if hash_type == "SHA256":
            db_status = save_evidence_to_db(
                case_id=1,
                file_path="Manual Hash Entry",
                sha256_hash=hash_value
            )
        else:
            db_status = "Not saved (Only SHA256 stored)"

    # 📝 Generate Report
    report = f"""
================ HASH ANALYSIS REPORT ================

Hash Value     : {hash_value}
Detected Type  : {hash_type}

Database Status: {db_status}

Reputation     : {reputation}
Risk Level     : {risk}

Recommendation :
- Preserve as evidence
- Compare with threat intelligence databases
- Perform deeper malware analysis

======================================================
"""

    return report
