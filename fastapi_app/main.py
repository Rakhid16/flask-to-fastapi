from joblib import load
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

model = load("../modeling/simple_model.pkl")                            # MODEL LAODED
templates = Jinja2Templates(directory = "templates")                    # HTML FILES
app.mount("/static", StaticFiles(directory="static"), name="static")    # STATIC FILES (CSS & JAVASCRIPT)

@app.get("/{sentence}")
def index(sentence:str):
  return {"hello" : sentence}

@app.get("/html_css_js/", response_class = HTMLResponse)
def page(request : Request):
  return templates.TemplateResponse("index.html", {"request" : request, "data" : "ini dari FastAPI"})

@app.post("/ml_serving")
def ml_serving(sentence : str):
  return {"Hasilnya adalah" : model.classify(sentence)}