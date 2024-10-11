from fastapi import APIRouter, HTTPException
from typing import Dict, List
from ..schemas.bus_route import BusRouteCreate, BusRoute
from ..crud.bus_route import create_bus_route, get_bus_route, get_bus_route_by_name, delete_bus_route, get_all_bus_route_names

router = APIRouter()

@router.post("/", response_model=BusRoute)
def create_route(route: BusRouteCreate):
    route_data = create_bus_route(route)
    return route_data

@router.get("/all", response_model=Dict[str, List[str]])
def read_all_route_names():
    route_names = get_all_bus_route_names()
    if not route_names:
        raise HTTPException(status_code=404, detail="No bus routes found")
    return route_names

@router.get("/{route_id}", response_model=BusRoute)
def read_route(route_id: str):
    route_data = get_bus_route(route_id)
    if not route_data:
        raise HTTPException(status_code=404, detail="Bus route not found")
    return route_data

@router.get("/by-name/{name:path}/{direction}", response_model=BusRoute)
def read_route_by_name(name: str, direction: int):
    route_data = get_bus_route_by_name(name, direction)
    if not route_data:
        raise HTTPException(status_code=404, detail="Bus route not found")
    return route_data

@router.delete("/{route_id}")
def remove_route(route_id: str):
    delete_message = delete_bus_route(route_id)
    return delete_message
