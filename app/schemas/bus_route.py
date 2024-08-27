from pydantic import BaseModel
from typing import List, Optional
from .bus_stop import BusStop

class BusRoute(BaseModel):
    id: str
    name: str
    direction: int
    origin: Optional[BusStop]
    destination: Optional[BusStop]
    stops: List[BusStop]
    stops_count: int

class BusRouteCreate(BaseModel):
    name: str
    direction: int
    origin: Optional[BusStop]
    destination: Optional[BusStop]
    stops: List[BusStop]
    stops_count: int
