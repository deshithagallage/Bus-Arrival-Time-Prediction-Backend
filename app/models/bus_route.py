from typing import List, Optional
from .bus_stop import BusStop

class BusRoute:
    def __init__(self, name: str, stops: List[BusStop], id: Optional[str] = None):
        self.id = id
        self.name = name
        self.stops = stops

    def to_dict(self):
        return {
            "name": self.name,
            "stops": [stop.to_dict() for stop in self.stops]
        }

    @staticmethod
    def from_dict(data: dict, id: Optional[str] = None):
        stops_data = data.get("stops", [])
        stops = [BusStop.from_dict(stop) for stop in stops_data]
        return BusRoute(
            id=id,
            name=data.get("name"),
            stops=stops
        )
