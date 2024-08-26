from fastapi import HTTPException
from ..core.firebase import firestore_db
from ..schemas.bus_route import BusRouteCreate, BusRoute
from ..schemas.bus_stop import BusStop
from .bus_stop import get_bus_stop

def create_bus_route(route: BusRouteCreate):
    route_ref = firestore_db.collection("bus_routes").document()  # Firestore auto-generates the ID
    route_ref.set({
        "name": route.name,
        "direction": route.direction,
        "origin_id": route.origin.id,
        "destination_id": route.destination.id,
        "stops_ids": [stop.id for stop in route.stops],
        "stops_count": route.stops_count
    })

    return BusRoute(
        id=route_ref.id,
        name=route.name,
        direction=route.direction,
        origin=route.origin,
        destination=route.destination,
        stops=route.stops,
        stops_count=route.stops_count
    )

def get_bus_route(route_id: str) -> BusRoute:
    route_ref = firestore_db.collection("bus_routes").document(route_id)
    route_doc = route_ref.get()

    if not route_doc.exists:
        return None

    route_data = route_doc.to_dict()
    stops_ids = route_data.get("stops_ids", [])

    stops = []
    for stop_id in stops_ids:
        stop = get_bus_stop(stop_id)
        if stop:
            stops.append(stop)
        else:
            print(f"Warning: Bus stop with id {stop_id} not found")

    origin = get_bus_stop(route_data.get("origin_id"))
    destination = get_bus_stop(route_data.get("destination_id"))

    if not origin:
        print("Warning: Origin bus stop not found")
    if not destination:
        print("Warning: Destination bus stop not found")

    return BusRoute(
        id=route_id,
        name=route_data.get("name"),
        direction=route_data.get("direction"),
        origin=origin if origin else BusStop(id="N/A", name="Unknown", longitude=0.0, latitude=0.0),
        destination=destination if destination else BusStop(id="N/A", name="Unknown", longitude=0.0, latitude=0.0),
        stops=stops,
        stops_count=route_data.get("stops_count")
    )

def delete_bus_route(route_id: str):
    route_ref = firestore_db.collection("bus_routes").document(route_id)
    route_doc = route_ref.get()

    if not route_doc.exists:
        raise HTTPException(status_code=404, detail=f"Bus route {route_id} not found.")

    route_ref.delete()

    return {"message": f"Bus route {route_id} deleted successfully."}
