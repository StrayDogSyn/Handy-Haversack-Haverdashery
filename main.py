"""
Main FastAPI application entry point.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Handy Haversack Haverdashery API",
    description="A Pathfinder TTRPG companion API for character management, dice rolling, and encounter generation",
    version="0.1.0",
)

# Configure CORS
origins = [
    "http://localhost:3000",  # React default
    "http://localhost:3001",  # Alternative port
    "http://localhost:5173",  # Vite default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Welcome to the Handy Haversack Haverdashery API",
        "status": "operational",
        "version": "0.1.0",
    }


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Import database initialization
from app.database import init_db

# Import routers
from app.api import characters, dice, encounters

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database on application startup"""
    init_db()

# Include routers
app.include_router(characters.router, prefix="/api/characters", tags=["characters"])
app.include_router(dice.router, prefix="/api/dice", tags=["dice"])
app.include_router(encounters.router, prefix="/api/encounters", tags=["encounters"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
