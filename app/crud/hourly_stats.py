import ast
from fastapi import HTTPException

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

def get_hourly_stats_by_route_and_day(route_name: str, day_of_week: str):
    # Query the Firestore collection for a single document
    hourly_stats_query = firestore_db.collection("hourly_stats") \
        .where("route_name", "==", route_name) \
        .where("day_of_week", "==", day_of_week).limit(1).get()  # Limit to 1 result

    # If no document is found, raise HTTP 404 exception
    if not hourly_stats_query:
        raise HTTPException(status_code=404, detail=f"Hourly stats not found for route '{route_name}' on '{day_of_week}'")

    # Extract the first document from the query result
    doc = hourly_stats_query[0]

    # Convert hourly_counts from string back to a dictionary
    hourly_counts_str = doc.to_dict().get("hourly_counts")
    
    # Convert hourly_counts from string back to a dictionary using ast.literal_eval
    try:
        hourly_counts = ast.literal_eval(hourly_counts_str)  # Safely evaluate the string as a dictionary
    except (ValueError, SyntaxError) as e:
        raise HTTPException(status_code=500, detail="Error decoding hourly counts")

    # Convert dictionary keys to strings for JSON compatibility
    hourly_counts_json = {str(k): v for k, v in hourly_counts.items()}
    
    hourly_stats = {
        "id": doc.id,
        "route_name": doc.to_dict().get("route_name"),
        "day_of_week": doc.to_dict().get("day_of_week"),
        "peak_hour": doc.to_dict().get("peak_hour"),
        "off_peak_hour": doc.to_dict().get("off_peak_hour"),
        "hourly_counts": hourly_counts_json
    }

    return hourly_stats
