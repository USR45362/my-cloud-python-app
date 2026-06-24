import subprocess
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from GitHub Codespaces!"}

# SECURED ENDPOINT: Defending against Command Injection
@app.get("/network/ping")
def ping_host(ip: str):
    try:
        # Pass parameters as an array. shell=False prevents command chaining (like '; rm -rf')
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            shell=False,
            capture_output=True,
            text=True,
            timeout=5
        )
        return {"status": "executed", "output": result.stdout}
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Ping timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))