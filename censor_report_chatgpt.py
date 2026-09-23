"""
You are working as a junior developer in a company that manages smart monitoring systems. You’ve been assigned a task to
generate a report using three sensor readings. The goal is to calculate the maximum, minimum, and average values using simple
variables and arithmetic operations only.
Use ChatGPT to help you generate this Python program with the following rules:
Ask ChatGPT to create three variables named sensor1, sensor2, and sensor3.
Assign the values:
sensor1 = 87
sensor2 = 90
sensor3 = 82
Ask it to calculate the maximum of these three values using only arithmetic (no built-in functions like max() or lists).
Ask it to calculate the minimum using the same logic (no min() function).
Then ask it to calculate the average of the three values and store it in a variable named average.
Finally, ask ChatGPT to print:
All sensor values
The maximum value
The minimum value
The average value
"""
# Store the three sensor readings
sensor1 = 87 # First sensor reading
sensor2 = 90 # Second sensor reading
sensor3 = 82 # Third sensor reading

# Calculate the maximum value using arithmetic comparisons
if sensor1 >= sensor2 and sensor1 >= sensor3: # Check if sensor1 is greater than or equal to both sensor2 and sensor3
    maximum = sensor1
elif sensor2 >= sensor1 and sensor2 >= sensor3: # Check if sensor2 is greater than or equal to both sensor1 and sensor3
    maximum = sensor2
else:
    maximum = sensor3

# Calculate the minimum value using arithmetic comparisons
if sensor1 <= sensor2 and sensor1 <= sensor3: # Check if sensor1 is less than or equal to both sensor2 and sensor3
    minimum = sensor1
elif sensor2 <= sensor1 and sensor2 <= sensor3: # Check if sensor2 is less than or equal to both sensor1 and sensor3
    minimum = sensor2
else:
    minimum = sensor3

# Calculate the average
average = (sensor1 + sensor2 + sensor3) / 3 # Calculate the average of the three sensor readings

# Print the sensor report
print("Sensor 1:", sensor1)
print("Sensor 2:", sensor2)
print("Sensor 3:", sensor3)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)