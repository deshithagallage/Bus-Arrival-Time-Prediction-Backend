from fastapi import APIRouter
from . import bus_route, bus_stop, predict, hourly_stats

router = APIRouter()

router.include_router(bus_route.router, prefix="/api/bus_routes", tags=["Bus Routes"])
router.include_router(bus_stop.router, prefix="/api/bus_stops", tags=["Bus Stops"])
router.include_router(predict.router, prefix="/api/model", tags=["Predictions"])
router.include_router(hourly_stats.router, prefix="/api/hourly_stats", tags=["Hourly Stats"])
