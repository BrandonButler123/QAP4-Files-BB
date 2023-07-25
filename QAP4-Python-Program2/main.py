# Program Description: Program to showcase annual sales on a graph
# Written By: Brandon Butler
# Date: July 18, 2023


#Imports
import matplotlib.pyplot as plt

#Define program constants

#Define a required functions

#Main program

sales = []
for month in range(1, 13):
    try:
        sales_value = float(input(f"Enter total sales for month {month}: $"))
        sales.append(sales_value)
    except ValueError:
        print("Invalid input. Please enter a valid sales amount.")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.figure()
plt.plot(months, sales, 'o-b', mec = 'r', mfc = 'r')
plt.title("Total Sales by Month")
plt.xlabel("Months")
plt.ylabel("Total Sales ($)")
plt.grid()
plt.xticks(months)
plt.show()

#Calculations

#Housekeeping
