#python project 

from fastapi import FastAPI
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