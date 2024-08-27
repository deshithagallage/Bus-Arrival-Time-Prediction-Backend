from typing import Optional

class BusStop:
    def __init__(self, name: str, longitude: str, latitude: str, id: Optional[str] = None):
        self.id = id
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "longitude": self.longitude,
            "latitude": self.latitude
        }

    @staticmethod
    def from_dict(data: dict, id: Optional[str] = None):
        return BusStop(
            id=id,
            name=data.get("name"),
            longitude=data.get("longitude"),
            latitude=data.get("latitude")
        )
