from pydantic import BaseModel

class HourlyStats(BaseModel):
    id: str
    route_name: str
    day_of_week: str
    peak_hour: int
    off_peak_hour: int  
    hourly_counts: str

class HourlyStatsCreate(BaseModel):
    route_name: str
    day_of_week: str
    peak_hour: int
    off_peak_hour: int
    hourly_counts: str
