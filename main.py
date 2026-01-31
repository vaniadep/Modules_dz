from fastapi import FastAPI
from routes.tasks import router as tasks_router

app = FastAPI(title="To-Do API")

app.include_router(tasks_router)
