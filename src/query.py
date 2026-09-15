import sqlite3
from pathlib import Path

project_root = Path(__file__).parent.parent

databese_file = project_root / "data" / "flights.db"

connection = sqlite3.connect(databese_file)

# destination = input("Enter your destination airport code: ").upper()

# -- How many flights are in the dataset?
query = "select count(*) from flights;"

# -- How many flights are nonstop or connecting?

# query ="""
# SELECT
#     flight_type,
#     COUNT(*) AS number_of_flights
# FROM flights
# GROUP BY flight_type;
# """

result = connection.execute(query)

rows = result.fetchall()

# print(rows)
for row in rows:
    print(row)


connection.close()