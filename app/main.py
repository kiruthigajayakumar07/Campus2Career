from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Campus2Career AI",
    description="Intelligent Career Development Ecosystem",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Campus2Career AI",
        "status": "Running",
        "portals": [
            "Student Portal",
            "Alumni Portal",
            "College Management Portal"
        ]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}