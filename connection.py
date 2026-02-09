from pydantic import BaseModel
class Base(BaseModel):
    name:str|None=None
    CS:int
    Math1:int
    Discrete:int
    Elctronics:int
    Creative_thinking:int
    Technical_writing:int

