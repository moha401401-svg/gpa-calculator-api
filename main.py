from fastapi import FastAPI
from service import insert_gpa,insert_gpa2
from connection import Base ,Base2
from database import initialize_db ,initialize_db2
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
    initialize_db2()


@app.get('/')
def hello():
    return {'message':'Welcome to GPA calculator'}

@app.post('/GPA')
def get(Grades:Base):
    return insert_gpa(Grades)

@app.post('/GPA2')
def get(Grades2:Base2):
    return insert_gpa2(Grades2)

