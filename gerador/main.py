import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from gen_routes import gen_router

load_dotenv()

app = FastAPI()
app.include_router(gen_router)


if __name__ == "__main__":
    api_host = os.getenv("API_HOST", "0.0.0.0")
    api_port = int(os.getenv("API_PORT", "3000"))
    uvicorn.run("main:app", host=api_host, port=api_port, reload=False)
