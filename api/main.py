from fastapi import FastAPI

from api.routers.healthcheck import router

app = FastAPI()

app.include_router(router)
