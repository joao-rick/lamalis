from fastapi import FastAPI

app = FastAPI()

from gen_routes import gen_router

app.include_router(gen_router)
