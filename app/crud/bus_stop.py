from ..core.firebase import firestore_db
from ..schemas.bus_stop import BusStopCreate, BusStop

def create_bus_stop(stop_data: BusStopCreate) -> BusStop:
    existing_stops = firestore_db.collection("bus_stops").where("name", "==", stop_data.name).stream()

    for existing_stop in existing_stops:
        stop_doc = existing_stop.to_dict()
        return BusStop(id=existing_stop.id, **stop_doc)

    stop_ref = firestore_db.collection("bus_stops").document()
    stop_ref.set({
        "name": stop_data.name,
        "longitude": stop_data.longitude,
        "latitude": stop_data.latitude
    })

    return BusStop(id=stop_ref.id, **stop_ref.get().to_dict())

def get_bus_stop(stop_id: str):
    stop_ref = firestore_db.collection("bus_stops").document(stop_id)
    stop_doc = stop_ref.get()

    if not stop_doc.exists:
        return None

    stop_data = stop_doc.to_dict()

    return BusStop(
        id=stop_id,
        name=stop_data.get("name"),
        longitude=stop_data.get("longitude"),
        latitude=stop_data.get("latitude")
    )

def get_bus_stop_by_name(name: str):
    stops_ref = firestore_db.collection("bus_stops")
    query = stops_ref.where(field_path="name", op_string="==", value=name).limit(1)
    results = query.stream()

    stop_doc = next(results, None)

    if not stop_doc:
        return None

    stop_data = stop_doc.to_dict()

    return BusStop(
        id=stop_doc.id,
        name=stop_data.get("name"),
        longitude=stop_data.get("longitude"),
        latitude=stop_data.get("latitude")
    )

def delete_bus_stop(stop_id: str):
    stop_ref = firestore_db.collection("bus_stops").document(stop_id)
    stop_doc = stop_ref.get()

    if not stop_doc.exists:
        return None
    
    stop_ref.delete()
    return {"message": f"Bus stop {stop_id} deleted successfully."}
