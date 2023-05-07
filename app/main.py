import uvicorn
from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def get_model():
    max = 30
    rand = random.randint(1, max)
    return {"free": random.randint(1, max),
            "occupied": max - rand}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
