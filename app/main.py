from fastapi import FastAPI

from blog import database, models
from blog.routers import authentication, user, blog

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
