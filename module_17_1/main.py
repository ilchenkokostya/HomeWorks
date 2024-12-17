from fastapi import FastAPI
from routers import task, user
import uvicorn

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
