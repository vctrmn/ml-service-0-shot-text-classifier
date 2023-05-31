import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import index

logs_format = "%(asctime)s [%(levelname)s] : %(message)s"
logging.basicConfig(format=logs_format, level=logging.INFO)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router)
