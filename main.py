from fastapi import FastAPI
from service import insert_gpa
from connection import Base
from database import initialize_db
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title='Welcome to GPA calcolator')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)
@app.on_event("startup")
def startup():
    initialize_db()


@app.get('/')
def hello():
    return {'message':'Welcome to GPA calcolator'}

@app.post('/GPA')
def get(Grades:Base):
    return insert_gpa(Grades)

