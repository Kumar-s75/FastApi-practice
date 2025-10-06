from fastapi import FastAPI
from pydantic import BaseModel
from typing import  List

app = FASTAPI()
# ///here w defined data structure using pudantic and python libraries
class Tea(BaseModel):
id: int
name: str
origin: str

teas:List[Tea] = []

# ///these are decorators
@app.get("/")
def read_root():
return {"message":"Welcome to Chai Code"}

@app.get("/teas")
def get_teas():
return teas

@app.post("/teas")
def add_tea():
teas.append(tea)
return tea

@app.put("/teas/{tea_id}")
def  updated_tea(tea_id:int,updated_tea:Tea):
for index,tea in enumerate(teas):
if tea.id==tea_id:
teas [index]= update_tea
return update_tea
return {"error":"tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
for index,tea in enumerate(teas):
if tea.id ==tea_id:
deleted = teas.pop(index)
return deleted
return {"error":"Tea not found"}




