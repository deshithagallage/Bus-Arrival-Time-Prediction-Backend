import os
from fastapi import FastAPI
from app.routers import router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Read the CORS origins from the .env file and split by comma
origins = os.getenv('CORS_ORIGINS').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from the origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(router)
