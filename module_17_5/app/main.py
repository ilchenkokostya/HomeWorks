from fastapi import FastAPI
from module_17_5.app.routers import task, user
import uvicorn

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)

# vicorn module_17_5.app.main:app --reloadu

# if __name__ == '__main__':
#     uvicorn.run("module_17_5.app.main:app", host='127.0.0.1', port=8000, reload=True)
