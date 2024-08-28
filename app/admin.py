import csv
from app.crud.bus_route import create_bus_route
from app.crud.bus_stop import create_bus_stop
from app.schemas.bus_route import BusRouteCreate
from app.schemas.bus_stop import BusStopCreate

def import_data_from_csv(file_path: str):        
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            if file:
                print("File found")
            
            row_count = 0
            for row in reader:
                # Extract and validate data from the row
                route_name = row.get('PublishedLineName')
                direction = int(row.get('DirectionRef', 0))
                origin_name = row.get('OriginName')
                origin_lat = float(row['OriginLat']) if row['OriginLat'] else None
                origin_long = float(row['OriginLong']) if row['OriginLong'] else None
                destination_name = row.get('DestinationName')
                destination_lat = float(row['DestinationLat']) if row['DestinationLat'] else None
                destination_long = float(row['DestinationLong']) if row['DestinationLong'] else None
                stop_points = eval(row.get('StopPoints', '[]'))
                stop_count = int(row.get('StopPointCount', 0))

                origin_stop = None
                if origin_name != '' or (origin_lat is not None and origin_long is not None):
                    origin_stop = create_bus_stop(BusStopCreate(
                        name=origin_name,
                        latitude=origin_lat,
                        longitude=origin_long
                    ))

                destination_stop = None
                if destination_name != '' or (destination_lat is not None and destination_long is not None):
                    destination_stop = create_bus_stop(BusStopCreate(
                        name=destination_name,
                        latitude=destination_lat,
                        longitude=destination_long
                    ))
                
                stops = []
                for stop in stop_points:
                    stop_lat = None
                    stop_long = None
                    stops.append(create_bus_stop(BusStopCreate(name=stop, latitude=stop_lat, longitude=stop_long)))

                # Create bus route
                create_bus_route(BusRouteCreate(
                    name=route_name,
                    direction=direction,
                    origin=origin_stop,
                    destination=destination_stop,
                    stops=stops,
                    stops_count=stop_count
                ))

                row_count += 1
            print(f"Processed {row_count} rows")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import_data_from_csv("app/Bus_Routes.csv")
