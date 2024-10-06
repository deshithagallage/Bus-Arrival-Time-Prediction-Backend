import os
import requests
from dotenv import load_dotenv

from ..schemas.predict import PredictionInput

# Load environment variables from .env file
load_dotenv()

def predict_arrival_time(input: PredictionInput):
    # Define the FastAPI URL
    url = os.getenv("MODEL_URL")

    # Convert the input to a dictionary (as FastAPI expects a JSON body)
    input_data = input.dict()

    try:
        # Send a POST request to the FastAPI endpoint
        response = requests.post(url, json=input_data)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None