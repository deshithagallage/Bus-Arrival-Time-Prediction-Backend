from fastapi import APIRouter, HTTPException
from ..schemas.bus_route import BusRouteCreate, BusRoute
from ..crud.bus_route import create_bus_route, get_bus_route, delete_bus_route

router = APIRouter()

@router.post("/", response_model=BusRoute)
def create_route(route: BusRouteCreate):
    route_data = create_bus_route(route)
    return route_data

@router.get("/{route_id}", response_model=BusRoute)
def read_route(route_id: str):
    route_data = get_bus_route(route_id)
    if not route_data:
        raise HTTPException(status_code=404, detail="Bus route not found")
    return route_data

@router.delete("/{route_id}")
def remove_route(route_id: str):
    delete_message = delete_bus_route(route_id)
    return delete_message
