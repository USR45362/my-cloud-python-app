import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from GitHub Codespaces!"}

# NEW VULNERABLE ENDPOINT: Command Injection Flaw
@app.get("/network/ping")
def ping_host(ip: str):
    # DANGER: We are concatenating user input ('ip') directly into an OS system shell command
    command = f"ping -c 1 {ip}"
    response = os.system(command)
    
    return {"status": "executed", "command_code": response}