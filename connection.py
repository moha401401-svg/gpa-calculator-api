from pydantic import BaseModel
class Base(BaseModel):
    name:str|None=None
    CS:float
    Math1:float
    Discrete:float
    Elctronics:float
    Creative_thinking:float
    Technical_writing:float
class Base2(BaseModel):
    name:str|None=None
    CS:float
    Discrete:float
    Elctronics:float
    Creative_thinking:float
    Technical_writing:float


