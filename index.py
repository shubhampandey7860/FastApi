from fastapi import FastAPI
from routers.note import note


app = FastAPI()

app.include_router(note)
