from typing import  List 
from fastapi import FastAPI,HTTPException
from models import User, Gender , Role ,UserUpadateRequest
from uuid import UUID
app=FastAPI()
db: list[User]=[
    User(
         id=UUID("46251876-984b-4f29-b713-9cf8783c13f4"),
         first_name="omar",
         last_name="alhamwi",
         gender=Gender.male,
         roles=[Role.student]),
    User(
         id=UUID("e5d89522-78eb-4b83-9def-3f30c955c47b"),
         first_name="Alex",
         last_name="Jones",
         gender=Gender.male,
         roles=[Role.admin,Role.user]),
   User(
        id =UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
        first_name="sami",
        last_name="queen",
        gender="female",
        roles= [Role.admin],)
]
@app.get("/")
async def root(): 
     return{"hello":"Omar"}

@app.get("/api/v1/users/")
async def fetch_users():
     return db

@app.post("/api/v1/users/{user_id}")
async def register_user(user:User):
     db.append(user)
     return{"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
     for user in db:
        if user.id ==user_id:
                db.remove(user)
                return
        raise HTTPException(
            status_code=404,
            detail= f" user with id :{user_id} does not exist ",
     )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update:UserUpadateRequest,user_id:UUID):
     for user in db:
          if user.id==user_id:
               if user_update.first_name is not None :
                  user.first_name = user_update.first_name
               if user_update.last_name is not None :
                  user.last_name = user_update.last_name
            #    if user_update.middle_name is not None :
            #       user.middle_name = user_update.middle_name
               if user_update.roles is not None :
                  user.roles = user_update.roles
               return
                         
          raise HTTPException(
            status_code=404,
            detail= f" user with id :{user_id} does not exist ",
     )