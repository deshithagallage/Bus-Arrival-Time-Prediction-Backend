from typing import List, Optional
from .bus_stop import BusStop

class BusRoute:
    def __init__(self, name: str, direction: int, stops: List[BusStop], 
                 origin: Optional[BusStop] = None, destination: Optional[BusStop] = None, 
                 stops_count: int = 0, id: Optional[str] = None):
        self.id = id
        self.name = name
        self.direction = direction
        self.origin = origin
        self.destination = destination
        self.stops = stops
        self.stops_count = stops_count

    def to_dict(self):
        return {
            "name": self.name,
            "direction": self.direction,
            "origin": self.origin.to_dict() if self.origin else None,
            "destination": self.destination.to_dict() if self.destination else None,
            "stops": [stop.to_dict() for stop in self.stops],
            "stops_count": self.stops_count
        }

    @staticmethod
    def from_dict(data: dict):
        stops_data = data.get("stops", [])
        stops = [BusStop.from_dict(stop) for stop in stops_data]
        return BusRoute(
            id=data.get("id"),
            name=data.get("name"),
            direction=data.get("direction"),
            origin=BusStop.from_dict(data.get("origin")) if data.get("origin") else None,
            destination=BusStop.from_dict(data.get("destination")) if data.get("destination") else None,
            stops=stops,
            stops_count=data.get("stops_count", len(stops))
        )
