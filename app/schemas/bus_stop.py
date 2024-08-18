from pydantic import BaseModel

class BusStop(BaseModel):
    id: str
    name: str
    longitude: float
    latitude: float

class BusStopCreate(BaseModel):
    name: str
    longitude: float
    latitude: float
