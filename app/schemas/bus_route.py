from pydantic import BaseModel
from typing import List
from .bus_stop import BusStopCreate, BusStop

class BusRoute(BaseModel):
    id: str
    name: str
    direction: int
    origin: BusStop
    destination: BusStop
    stops: List[BusStop]
    stops_count: int

class BusRouteCreate(BaseModel):
    name: str
    direction: int
    origin: BusStop
    destination: BusStop
    stops: List[BusStop]
    stops_count: int
