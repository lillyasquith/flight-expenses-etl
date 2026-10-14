# Flight Expenses ETL

## Project Overview

This project is a beginner ETL and a little bit of data analysis project using flight itinerary data.

The goal is to practice extracting, transforming, and loading data using Python, Pandas, and SQLite, and then use SQL to perform some basic data analysis.


## Project Workflow

Raw CSV
   ↓
Extract
   ↓
Transform
   ↓
Cleaned CSV
   ↓
Load into SQLite
   ↓
SQL Analysis


## Technologies

- Python
- Pandas
- SQLite
- SQL
- Git/GitHub


## Project Structure

flight-expenses-etl
│
├── data
│   ├── raw
│   │   └── itineraries-min-100k.csv
│   │
│   ├── processed
│   │   └── flights_cleaned.csv
│   │
│   └── flights.db
│
├── src
│   ├── extract.py
│   ├── load.py
│   └── query.py
│
├── sql
│   └── analysis.sql
│
├── .gitignore
└── README.md


## ETL Process

### Extract

The project reads the raw flight itinerary CSV file using Pandas.

### Transform

The data is transformed by:

- Selecting useful columns
- Renaming columns to snake_case
- Converting flight and search dates to datetime values
- Calculating additional fees
- Creating a flight type column for nonstop and connecting flights

### Load

The cleaned data is saved as a CSV file and loaded into a SQLite database called `flights.db`.

The cleaned data is stored in a table called `flights`.


## SQL Analysis

The project uses SQL to perform some basic data analysis, such as:

- How many flights are in the dataset?
- How many flights are nonstop or connecting?
- Other basic flight and fare analysis (To be continued)


## What I Learned

This project helped me practice:

- Python
- Pandas
- Data cleaning
- File paths
- ETL concepts
- SQLite databases
- SQL queries
- Basic data analysis
- Git and GitHub
