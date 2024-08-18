from pydantic import BaseModel
from typing import List
from .bus_stop import BusStopCreate, BusStop

class BusRoute(BaseModel):
    id: str
    name: str
    stops: List[BusStop]

class BusRouteCreate(BaseModel):
    name: str
    stops: List[BusStopCreate]
