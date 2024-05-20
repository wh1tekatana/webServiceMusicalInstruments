from fastapi import FastAPI
from app import models, routers
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)