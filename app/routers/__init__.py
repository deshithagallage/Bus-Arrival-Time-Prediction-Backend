from fastapi import APIRouter
from . import bus_route, bus_stop

router = APIRouter()

router.include_router(bus_route.router, prefix="/api/bus_routes", tags=["Bus Routes"])
router.include_router(bus_stop.router, prefix="/api/bus_stops", tags=["Bus Stops"])
