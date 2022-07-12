from os import stat
from fastapi import FastAPI, HTTPException, Path
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getId/{user_id}")
async def get_id(user_id: int = Path(None, description = "Digite o id que deseja procurar: ", gt= 0)):
    with open ("db.json", "r", encoding= "utf-8") as file:
        bd = json.load(file)
    for user in bd:
        if user["user_id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User id not found! ;-;")

@app.get("/getAll")
async def get_all():
    with open ("db.json", "r", encoding= "utf-8") as file:
        bd = json.load(file)
    return bd

@app.post("/create_user")
async def create_user(new_user: dict):
    try:
        with open ("db.json", "r", encoding= "utf-8") as file:
            bd = json.load(file)
        new_user["user_id"] = len(bd) + 1
        
        bd.append(new_user)
        with open("db.json", "w", encoding= "utf-8") as file:
            json.dump(bd, file)
        
        return {"status" : True}
    except:
        return {"status" : False}
        
@app.put("/update_user/{user_id}")
async def update_user(user_id : int, up_dict : dict):
    try:
        with open ("db.json", "r", encoding= "utf-8") as file:
            bd = json.load(file)

        for index, user in enumerate(bd):
            if user_id == user["user_id"]:
                up_dict["user_id"] = user_id
                bd[index] = up_dict

        with open("db.json", "w", encoding= "utf-8") as file:
            json.dump(bd, file)
            
        return {"status" : True}
            
    except:
        return {"status" : False}
        
@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    try:
        with open ("db.json", "r", encoding= "utf-8") as file:
            bd = json.load(file)
        for index, user in enumerate(bd):
            if user_id == user["user_id"]:
                del bd[index]
        with open("db.json", "w", encoding= "utf-8") as file:
            json.dump(bd, file)
            
        return {"status": True}    
    except:
        
        return {"status" : False}
