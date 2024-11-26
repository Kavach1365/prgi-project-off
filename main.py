from fastapi import FastAPI
from routes.routes import router

app = FastAPI()

# Include routers
app.include_router(router)
