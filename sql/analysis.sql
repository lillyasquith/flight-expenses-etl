-- How many flights are in the dataset?
--  select count(*) from flights;

-- How many flights are nonstop or connecting?
SELECT
    flight_type,
    COUNT(*) AS number_of_flights
FROM flights
GROUP BY flight_type;