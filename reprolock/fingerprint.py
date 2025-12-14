import platform
import sys
import hashlib
import json

def capture_environment():
    env = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "machine": platform.machine(),
    }
    env_hash = hashlib.sha256(json.dumps(env, sort_keys=True).encode()).hexdigest()
    env["hash"] = env_hash
    return env

if __name__ == "__main__":
    env = capture_environment()
    print(json.dumps(env, indent=2))
