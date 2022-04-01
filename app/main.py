from turtle import title
from fastapi import FastAPI
from .routers import signer, verifier


app = FastAPI(
    title="digisign-api"
)

app.include_router(signer.router)
app.include_router(verifier.router)
