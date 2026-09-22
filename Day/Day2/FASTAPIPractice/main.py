#python project 

from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

@app.get("/")
def Home():
    return {"page ":"Home "}

@app.get("/about")
def about():
    return{"page":"about","author":"Master Kushal"}

@app.get("/health")
def health():
    return{"status":"ok"}

#post request
@app.post("/create")
def create_something():
    return{"message":"created"}

#path parameters 
@app.get("/students/{usn}")
def get_result(usn):
    return{"result: ":"Distinction","usn":usn}

#path parameters with type int 
@app.get("/candidate/{rollno}")
def get_candidate(rollno:int):
    return{"result: ":"Distinction","rollno":rollno,"type":str(type(rollno))}

#pydantic Modle

class Item(BaseModel):
    name:str
    price:float
    in_stock:bool=True

@app.post("/items")
def create_item(item:Item):
    return{"received":item,"total_price":item.price*1.8}