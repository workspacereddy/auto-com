from fastapi import FastAPI
import uvicorn
from threading import Thread
import asyncio
from git_committer import setup_and_run_committer

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GitHub Auto Commit App is Running."}

@app.on_event("startup")
async def start_background_task():
    Thread(target=setup_and_run_committer, daemon=True).start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
