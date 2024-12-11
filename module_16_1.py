from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/", tags=["Главная страница"])
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin", tags=["Страница администратора 👨‍💼"])
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}", tags=["Страница пользователя 🙍"])
async def get_user_number(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user", tags=["Страница пользователя 🙍"])
async def get_user_info(username: str = 'NoneName', age: int = 0) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


if __name__ == '__main__':
    uvicorn.run("module_16_1:app", host='127.0.0.1', port=8000, reload=True)
