from ..core.firebase import firestore_db
from ..schemas.hourly_stats import HourlyStatsCreate

def create_hourly_stats(hourly_stats: HourlyStatsCreate):
    hourly_stats_ref = firestore_db.collection("hourly_stats").document()  # Firestore auto-generates the ID
    hourly_stats_ref.set({
        "route_name": hourly_stats.route_name,
        "day_of_week": hourly_stats.day_of_week,
        "peak_hour": hourly_stats.peak_hour,
        "off_peak_hour": hourly_stats.off_peak_hour,
        "hourly_counts": hourly_stats.hourly_counts
    })

    return {
        "id": hourly_stats_ref.id,
        "route_name": hourly_stats.route_name,
        "day_of_week": hourly_stats.day_of_week,
        "peak_hour": hourly_stats.peak_hour,
        "off_peak_hour": hourly_stats.off_peak_hour,
        "hourly_counts": hourly_stats.hourly_counts
    }
