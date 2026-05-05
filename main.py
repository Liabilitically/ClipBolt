import multiprocessing
import sys
import pyperclip
import requests
import time
import uvicorn
import os
from fastapi import FastAPI, Request, Header, HTTPException

# --- AUTO-CONFIG GENERATOR ---
def load_config():
    if not os.path.exists("config.txt"):
        with open("config.txt", "w") as f:
            f.write("API_KEY=Secret123\nPORT=8000")
        return "Secret123", 8000
    
    config = {}
    with open("config.txt", "r") as f:
        for line in f:
            name, value = line.partition("=")[::2]
            config[name.strip()] = value.strip()
    return config.get("API_KEY", "Secret123"), int(config.get("PORT", 8000))

API_KEY, PORT = load_config()

# --- SERVER ---
app = FastAPI()
latest_clip = {"text": "No data yet"}

@app.get("/paste")
async def get_clip(x_api_key: str = Header(None)):
    if x_api_key != API_KEY: raise HTTPException(status_code=403)
    return latest_clip

@app.post("/copy")
async def post_clip(request: Request, x_api_key: str = Header(None)):
    if x_api_key != API_KEY: raise HTTPException(status_code=403)
    global latest_clip
    latest_clip = await request.json()
    return {"status": "success"}

@app.post("/from-phone")
async def from_phone(request: Request, x_api_key: str = Header(None)):
    if x_api_key != API_KEY: raise HTTPException(status_code=403)
    data = await request.json()
    pyperclip.copy(data.get("text", ""))
    return {"status": "success"}

def run_server():
    # Tell uvicorn specifically to NOT use its default logging config
    # which is what's looking for the 'isatty' attribute.
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=PORT, 
        log_config=None,  # This is the magic fix
        access_log=False  # Disabling logs entirely for the background process
    )

# --- MONITOR ---
def run_monitor():
    last_clip = ""
    server_url = f"http://127.0.0.1:{PORT}/copy"
    while True:
        try:
            current_clip = pyperclip.paste()
            if current_clip != last_clip and current_clip.strip() != "":
                requests.post(server_url, json={"text": current_clip}, headers={"x-api-key": API_KEY})
                last_clip = current_clip
        except: pass
        time.sleep(1)


if __name__ == "__main__":
    # Fix for --noconsole mode: redirect stdout/stderr to nowhere
    # so libraries don't crash when trying to write to the missing console.
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")

    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=run_server)
    p2 = multiprocessing.Process(target=run_monitor)
    p1.start()
    p2.start()
    p1.join()
    p2.join()