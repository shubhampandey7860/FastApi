from fastapi import APIRouter, Request
from models.note import Note
from config.db import *
from schema.note import notesEntity, noteEntity
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

note = APIRouter()

note.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def index(request: Request):
    docs = mycol.find({})
    new_docs = []
    for doc in docs:
        new_docs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"],

        })

    return templates.TemplateResponse("index.html", {"request": request, "new_docs": new_docs,"docs":docs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    data = mycol.insert_one(formDict)
    return {"sucess": True}
