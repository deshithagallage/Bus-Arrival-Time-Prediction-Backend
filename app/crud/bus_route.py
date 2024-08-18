from ..core.firebase import db
from ..schemas.bus_route import BusRouteCreate, BusRoute
from .bus_stop import create_bus_stop, get_bus_stop, delete_bus_stop

def create_bus_route(route: BusRouteCreate):
    route_ref = db.collection("bus_routes").document()  # Firestore auto-generates the ID
    route_ref.set({"name": route.name})

    stops = []
    for stop_data in route.stops:
        stop = create_bus_stop(stop_data)
        stops.append(stop)

    return BusRoute(id=route_ref.id, name=route.name, stops=stops)

def get_bus_route(route_id: str):
    route_ref = db.collection("bus_routes").document(route_id)
    route_doc = route_ref.get()

    if not route_doc.exists:
        return None

    stops_ref = route_ref.collection("stops")
    stops_docs = stops_ref.stream()

    stops = []
    for stop_doc in stops_docs:
        stop = get_bus_stop(stop_doc.id)
        if stop:
            stops.append(stop)

    route_data = route_doc.to_dict()
    return BusRoute(id=route_id, name=route_data["name"], stops=stops)

def delete_bus_route(route_id: str):
    route_ref = db.collection("bus_routes").document(route_id)
    route_ref.delete()
    return {"message": f"Bus route {route_id} deleted successfully."}
