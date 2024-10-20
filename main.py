from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)