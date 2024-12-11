from fastapi import FastAPI, Path
from typing import Annotated, Optional
import uvicorn

app = FastAPI()


@app.get("/", tags=["Главная страница"])
async def get_main_page() -> str:
    return "Главная страница"


@app.get("/user/admin", tags=["Страница администратора 👨‍💼"])
async def get_main_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}", tags=["Страница пользователя 🙍"])
async def get_admin_page(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}", tags=["Страница пользователя 🙍"])
async def get_user_number(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


if __name__ == '__main__':
    uvicorn.run("module_16_2:app", host='127.0.0.1', port=8000, reload=True)
