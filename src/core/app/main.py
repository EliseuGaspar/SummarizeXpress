from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(
    title="SummarizeXpress",
    description="Plataforma de criação de resumos autonoma",
    version="0.1",
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
