from fastapi import FastAPI
from routers.student_router import Router
from database import Base,engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

router = Router().router
app.include_router(router)