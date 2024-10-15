#!/usr/bin/env python3

import csv

# Problem 1

with open('CO-OPS__8729108__wl.csv', 'r')
  reader
import csv


highest_water_level = float('-inf') # Create variable for water level and set it to negative infinity so any subsequent values will be larger
highest_date_time = "" # Create variable for date and time that will correspond with the highest water level

with open("CO-OPS__8729108__wl.csv", 'r') as file:
    reader = csv.reader(file)
    header = next(reader) # Skip header row
    
    for row in reader:
            date_time = row[0]
            try:
                water_level = float(row[1])
            except ValueError:
                continue
                
            if water_level > highest_water_level:
                highest_water_level = water_level
                highest_date_time = date_time
            
print(f"The highest water level was {highest_water_level} ft. observed on {highest_date_time}")
