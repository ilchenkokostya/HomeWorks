from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
import uvicorn

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/user/admin")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    users[str(int(max(users.keys())) + 1)] = f"Имя: {username}, возраст: {age}"
    return f"User {max(users.keys())} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")],
        user_id: Annotated[int, Path(ge=1, description="Enter User ID", example="1")]) -> str:
    if str(user_id) not in users.keys():
        raise HTTPException(status_code=404, detail="User ID not found")
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, description="Enter User ID", example="1")]) -> str:
    if str(user_id) not in users.keys():
        raise HTTPException(status_code=404, detail="User ID not found")
    return f"User {user_id} {users.pop(str(user_id))} has been deleted"


if __name__ == '__main__':
    uvicorn.run("module_16_3:app", host='127.0.0.1', port=8000, reload=True)
