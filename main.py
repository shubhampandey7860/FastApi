# from fastapi import FastAPI, Request
#
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient
#
# conn = MongoClient("mongodb://localhost:27017")
# mydb = conn["Notes"]
# mycol = mydb["note"]
#
# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")
#
#
# @app.get("/")
# def Hello():
#     return {"data": "Jay Shri Ram"}
#
#
# @app.get("/index", response_class=HTMLResponse)
# def index(request: Request):
#     docs = mycol.find({})
#     new_docs = []
#     for doc in docs:
#         new_docs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#
#         })
#
#     return templates.TemplateResponse("index.html", {"request": request,"new_docs": new_docs})
