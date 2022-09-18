
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session,select
from database import engine
from models.question import Question

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
def root(request:Request):
    return templates.TemplateResponse('index.html', {'request':request})
    
@app.get('/quiz')
def get_quiz():
    with Session(engine) as session:
        statement = select(Question)
        results = session.exec(statement)
        return [result.dict() for result in results]

