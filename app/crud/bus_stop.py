from ..core.firebase import db
from ..schemas.bus_stop import BusStopCreate, BusStop

def create_bus_stop(stop_data: BusStopCreate):
    stop_ref = db.collection("bus_stops").document()
    stop_ref.set({
        "name": stop_data.name,
        "longitude": stop_data.longitude,
        "latitude": stop_data.latitude
    })
    return BusStop(id=stop_ref.id, **stop_ref.get().to_dict())

def get_bus_stop(stop_id: str):
    stop_ref = db.collection("bus_stops").document(stop_id)
    stop_doc = stop_ref.get()

    if not stop_doc.exists:
        return None

    stop_data = stop_doc.to_dict()
    return BusStop(id=stop_id, **stop_data)

def delete_bus_stop(stop_id: str):
    stop_ref = db.collection("bus_stops").document(stop_id)
    stop_doc = stop_ref.get()

    if not stop_doc.exists:
        return None
    
    stop_ref.delete()
    return {"message": f"Bus stop {stop_id} deleted successfully."}
