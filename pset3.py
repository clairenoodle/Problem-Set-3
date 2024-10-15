#!/usr/bin/env python3

import csv

# Problem 1

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

# Problem 2

# Create variables
highest_water_level = float('-inf')
lowest_water_level = float('inf')
highest_date_time = ""
lowest_date_time = ""
avg_water_level = 0
water_levels_list = []

with open("CO-OPS__8729108__wl.csv", 'r') as file:
    reader = csv.reader(file)
    header = next(reader) # Skip header row
    
    for row in reader:
            date_time = row[0]
            try:
                water_level = float(row[1])
            except ValueError:
                continue
            
            water_levels_list.append(water_level) #Create a list of the water level values
                
            if water_level > highest_water_level:
                highest_water_level = water_level
                highest_date_time = date_time
                
            if water_level < lowest_water_level:
                lowest_water_level = water_level
                lowest_date_time = date_time

# Calculate the average
avg_water_level = sum(water_levels_list) / len(water_levels_list) if water_levels_list else None 

print(f"The highest water level was {highest_water_level} ft. observed on {highest_date_time}.")
print(f"The lowest water level was {lowest_water_level} ft. observed on {lowest_date_time}.")
print(f"The average water level is {avg_water_level} ft.")

# Problem 3

# Create variables
fastest_rise = float('-inf')
fastest_date_time = ""
previous_water_level = None


with open("CO-OPS__8729108__wl.csv", 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    
    for row in reader:
        date_time = row[0]
        try:
            water_level = float(row[1])
        except ValueError:
            continue
    
        if previous_water_level != None: # Previous water level must exist , i.e. start from the second line
            change = water_level - previous_water_level
        
            if change > fastest_rise: 
                fastest_rise = change
                fastest_date_time = date_time
                
    
        previous_water_level = water_level # Reset for the next iteration
    
print(f"The fastest rise in water level per 6-minute period was {fastest_rise} ft. on {fastest_date_time}.")


                
                
