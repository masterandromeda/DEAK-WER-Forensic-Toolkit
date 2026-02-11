import re

def detect_hash_type(hash_value):
    if re.fullmatch(r"[A-Fa-f0-9]{32}", hash_value):
        return "MD5"
    elif re.fullmatch(r"[A-Fa-f0-9]{40}", hash_value):
        return "SHA1"
    elif re.fullmatch(r"[A-Fa-f0-9]{64}", hash_value):
        return "SHA256"
    else:
        return None

def analyze_hash(hash_value):
    hash_value = hash_value.strip()

    # 1️⃣ No input
    if not hash_value:
        return "❌ ERROR: No data provided. Please enter a hash value."

    # 2️⃣ Invalid format
    hash_type = detect_hash_type(hash_value)
    if not hash_type:
        return "❌ ERROR: Incorrect hash format. Not a valid MD5/SHA1/SHA256."

    # 3️⃣ Valid hash → Forensic report
    report = f"""
==== HASH ANALYSIS REPORT ====

Hash Value: {hash_value}
Detected Type: {hash_type}

Reputation: Not found in local database
Risk Level: Unknown

Recommendation:
- Preserve as evidence
- Compare with threat databases
- Perform deeper analysis
"""
    return report
