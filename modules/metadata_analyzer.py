import os
import time

def get_metadata(file_path):
    try:
        info = os.stat(file_path)
        return {
            "Size (bytes)": info.st_size,
            "Created": time.ctime(info.st_ctime),
            "Modified": time.ctime(info.st_mtime)
        }
    except:
        return "Error reading metadata"
