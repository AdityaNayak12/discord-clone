from fastapi import FastAPI
from app.database.init_db import init_db
from app.api.auth import router as auth_router

app = FastAPI(
    title="Discord Clone API",
    description="A minimal Discord clone backend built with FastAPI",
    version="1.0.0"
)

# Include routers
app.include_router(auth_router)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {
        "message": "Welcome to Discord Clone API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
