from fastapi import APIRouter, HTTPException
from ..schemas.bus_stop import BusStopCreate, BusStop
from ..crud.bus_stop import create_bus_stop, get_bus_stop, delete_bus_stop

router = APIRouter()

@router.post("/", response_model=BusStop)
def create_stop(stop: BusStopCreate):
    stop_data = create_bus_stop(stop)
    return stop_data

@router.get("/{stop_id}", response_model=BusStop)
def read_stop(stop_id: str):
    stop_data = get_bus_stop(stop_id)
    if not stop_data:
        raise HTTPException(status_code=404, detail="Bus stop not found")
    return stop_data

@router.delete("/{stop_id}")
def remove_stop(stop_id: str):
    delete_message = delete_bus_stop(stop_id)
    if not delete_message:
        raise HTTPException(status_code=404, detail="Bus stop not found")
    return delete_message
