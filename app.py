from fastapi import FastAPI
import os

app = FastAPI()

ENV_KEYS = {
    "key1": os.getenv("KEY1"),
    "key2": os.getenv("KEY2"),
    "key3": os.getenv("KEY3"),
    "key4": os.getenv("KEY4"),
}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test")
def test():
    return {
        "message": "Env variables loaded",
        "values": [{"key": key, "value": value} for key, value in ENV_KEYS.items()],
    }
