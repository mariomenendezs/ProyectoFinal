-- Drop the view if it exists
DROP VIEW IF EXISTS Summarize_yellow_taxi_trips;

-- Create the view
CREATE VIEW Summarize_yellow_taxi_trips AS
SELECT 
    vendorid,
    date_trunc('hour', tpep_pickup_datetime) AS pick_hour,
    AVG(passenger_count) AS avg_passenger_count,
    SUM(passenger_count) AS total_passenger_count,
    AVG(trip_distance) AS avg_trip_distance,
    SUM(trip_distance) AS total_trip_distance,
    AVG(fare_amount) AS avg_fare_amount,
    SUM(fare_amount) AS total_fare_amount,
    AVG(total_amount) AS avg_total_amount,
    SUM(total_amount) AS sum_total_amount,
    COUNT(*) AS total_trips
FROM 
    yellow.yellow_taxi_trips
WHERE 
    tpep_pickup_datetime >= '2023-01-01'
GROUP BY 
    vendorid,
    DATE(tpep_pickup_datetime),
    date_trunc('hour', tpep_pickup_datetime);