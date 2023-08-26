from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import ExpiredSignatureError, InvalidSignatureError
import jwt
from datetime import datetime, timedelta
from model import ToDo
from mgdb import collection
from pydantic import BaseModel

app = FastAPI()

class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        username = payload.get("sub")
    except (ExpiredSignatureError, InvalidSignatureError):
        raise credentials_exception
    if username is None:
        raise credentials_exception
    return username

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "USERNAME" and form_data.password == "my-PASSWORD":
        access_token_expires = timedelta(minutes=30)
        access_token = jwt.encode(
            {"sub": form_data.username, "exp": datetime.utcnow() + access_token_expires},
            "secret",
            algorithm="HS256"
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/toDos")
def get_todos(user: str = Depends(get_user)):
    return {"message":"no data"}

@app.post("/toDos")
def create_todo(toDo: ToDo, user: str = Depends(get_user)):
    collection.insert_one(toDo.dict())
    return toDo

@app.put("/toDos/{id}")
def update_todo(id: int, toDo: ToDo, user: str = Depends(get_user)):
    collection.update_one({'id': id}, {'$set': toDo.dict()})
    return toDo
 
@app.delete("/toDos/{id}")
def delete_todo(id: int, user: str = Depends(get_user)):
    collection.delete_one({'id': id})
    return {'message': 'Todo deleted'}