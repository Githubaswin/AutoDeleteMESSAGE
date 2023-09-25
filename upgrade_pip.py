# upgrade_pip.py
import subprocess

def upgrade_pip():
    try:
        subprocess.check_call(["/opt/render/project/src/.venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call(["/opt/render/project/src/.venv/bin/python", "-m", "pip", "install", "Pyrogram==2.0.106", "Tgcrypto==1.2.5", "dotenv==0.18.0"])
        print("Pip and required packages upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    upgrade_pip()
