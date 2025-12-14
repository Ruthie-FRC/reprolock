import hashlib
import json

def hash_output(data):
    """Hash any Python object (dict, list, etc.)"""
    serialized = json.dumps(data, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()

def check_output(data, baseline_hash):
    """Compare current output hash to baseline"""
    current_hash = hash_output(data)
    if current_hash != baseline_hash:
        raise ValueError(
            f"Output changed!\nExpected hash: {baseline_hash}\nGot hash: {current_hash}"
        )
    print("Output matches baseline ✅")
