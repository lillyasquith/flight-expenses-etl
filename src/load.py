import pandas as pd
import sqlite3
from pathlib import Path

project_root = Path(__file__).parent.parent

cleaned_file = project_root / "data" / "processed" / "flight_cleaned.csv" 

flight_data = pd.read_csv(cleaned_file)

#check the data
print(flight_data.head())

#create the database
database_file = project_root / "data" / "flights.db"

#connect to the database
connection = sqlite3.connect(database_file)

#load the data into a table
flight_data.to_sql("flights", connection, if_exists="replace", index=False)

#close the connection
connection.close

