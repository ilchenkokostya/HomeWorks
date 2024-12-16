from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, ConfigDict
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int = Field(ge=1, description="Enter User ID")
    username: str = Field(min_length=5, max_length=20, description="Enter username")
    age: int = Field(ge=18, le=120, description="Enter age")
    # запрет на доп поля
    model_config = ConfigDict(extra='forbid')


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})


@app.post("/")
async def post_user(request: Request, username: str = Form(), age: int = Form()) -> HTMLResponse:
    new_user_id = max((i.id for i in users), default=0) + 1
    user = User(id=new_user_id, username=username, age=age)
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


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
    uvicorn.run("module_16_5:app", host='127.0.0.1', port=8000, reload=True)
