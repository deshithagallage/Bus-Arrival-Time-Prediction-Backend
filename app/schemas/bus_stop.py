from typing import Optional
from pydantic import BaseModel

class BusStop(BaseModel):
    id: str
    name: str
    longitude: Optional[float]
    latitude: Optional[float]

class BusStopCreate(BaseModel):
    name: str
    longitude: Optional[float]
    latitude: Optional[float]
