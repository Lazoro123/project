from fastapi import FastAPI
from backend.routes import auth, vm
app = FastAPI()
app.include_router(auth.router, prefix="/auth")
# keep other routers...

