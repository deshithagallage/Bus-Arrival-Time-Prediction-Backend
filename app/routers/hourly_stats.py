from fastapi import APIRouter, HTTPException
from ..crud.hourly_stats import get_hourly_stats_by_route_and_day

router = APIRouter()

@router.get("/{route_name}/{day_of_week}")
def read_hourly_stats(route_name: str, day_of_week: str):
    try:
        hourly_stats = get_hourly_stats_by_route_and_day(route_name, day_of_week)
        return hourly_stats
    except HTTPException as e:
        raise e
