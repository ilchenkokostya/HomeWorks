from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict
import uvicorn

app = FastAPI()

users = []


class User(BaseModel):
    id: int = Field(ge=1, description="Enter User ID")
    username: str = Field(min_length=5, max_length=20, description="Enter username")
    age: int = Field(ge=18, le=120, description="Enter age")
    # запрет на доп п
    model_config = ConfigDict(extra='forbid')


@app.get("/user")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def post_user(user: User) -> list:
    user.id = max((i.id for i in users), default=0) + 1
    users.append(user)
    return users


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, user: User) -> list:
    for i in users:
        if i.id == user_id:
            i.username = user.username
            i.age = user.age
            return users
    else:
        raise HTTPException(status_code=404, detail="User ID not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> list:
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return users
    else:
        raise HTTPException(status_code=404, detail="User ID not found")


if __name__ == '__main__':
    uvicorn.run("module_16_4:app", host='127.0.0.1', port=8000, reload=True)
