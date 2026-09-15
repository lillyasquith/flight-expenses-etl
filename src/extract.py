import pandas as pd
from pathlib import Path

# Find my main project folder
project_root = Path(__file__).parent.parent
#------------------
# EXTRACT THE DATA
#------------------

def extract_data():
    file_path = project_root / "data" / "raw" / "itineraries-min-100k.csv"
    # file_path = Path("data/raw/itineraries-min-100k.csv")

    df = pd.read_csv(file_path)
    return df

flight_data = extract_data()

#------------------
# INPECT THE DATA
#------------------

# print(len(flight_data))#number of rows 
# print(len(flight_data.columns)) #number of columns
#OR flight_data.shape will return number of rows and column together like this (100000, 27)

# print("Shape:")
# print(flight_data.shape) #Properties/attributes → don't use ()

# print("\nFirst 5 rows:")
# print(flight_data.head()) #Functions/methods → use ()

# print("\nData types:")
# print(flight_data.dtypes)

# print("\nMissing values:")
# print(flight_data.isnull().sum())

# print("\nDuplicate rows:")
# print(flight_data.duplicated().sum())

# print("\nColumn names:")
# print(flight_data.columns.tolist())


# ------------------
# TRANSFORM THE DATA
# ------------------

#1. Keep important columns

columns_list = [
    "legId",
    "searchDate",
    "flightDate",
    "startingAirport",
    "destinationAirport",
    "segmentsAirlineName",
    "baseFare",
    "totalFare",
    "isBasicEconomy",
    "isRefundable",
    "isNonStop",
    "totalTravelDistance",
    "seatsRemaining",
    "segmentsCabinCode"
]

#rather than ASSIGN the list directly to flight_data like this: flight_data = columns_list => This replaces your DataFrame with the list of column names => A Python list does not have .columns, so this will cause an error. Instead, use the list to SELECT from the DataFrame like this: 

flight_data = flight_data[columns_list]

print(flight_data.columns)

# 2.Rename the columns with snake_case:

flight_data = flight_data.rename(columns={
    "ledId": "flight_id",
    "searchDate": "search_date",
    "flightDate": "flight_date",
    "startingAirport": "origin",
    "destinationAirport": "destination",
    "segmentsAirlineName": "airline",
    "baseFare": "base_fare",
    "totalFare": "total_fare",
    "isBasicEconomy": "is_basic_economy",
    "isRefundable": "is_refundable",
    "isNonStop": "is_nonstop",
    "totalTravelDistance": "distance",
    "seatsRemaining": "seats_remaining",
    "segmentsCabinCode": "cabin"
})

print(flight_data.columns)

# 3.Convert dtpypes of the dates

flight_data["search_date"] = pd.to_datetime(flight_data["search_date"])
flight_data["flight_date"] = pd.to_datetime(flight_data["flight_date"])

print(flight_data.dtypes)
print(flight_data["flight_date"].dt.year) 
#.dt gives access to date/time properties in Pandas

# 4. Create additional_fees column

flight_data["additional_fees"] = (flight_data["total_fare"] - flight_data["base_fare"])

#Check data with those 3 columns
print(flight_data[["base_fare", "total_fare", "additional_fees"]].head())
# NOTE: 
# Selecting ONE column → one pair of brackets
# Selecting MULTIPLE columns → two pairs of brackets

# 5. Create flight_type column

flight_data["flight_type"] = flight_data["is_nonstop"].map({
    True: "Nonstop",
    False: "Connecting"
})
# .map() will replace values of every item in an iterable (like a list, tuple, or dictionary)according to a mapping.

#Check data with the new flight_type column
print(flight_data["flight_type"].value_counts())
# value_counts() counts how many times each value occurs.

# 6.Save the processed CSV

cleaned_file = project_root / "data" / "processed" / "flight_cleaned.csv"
flight_data.to_csv(cleaned_file, index=False)

