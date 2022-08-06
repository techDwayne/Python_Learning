#Program to demonstrate the use of functions in the datetime module
print("Importing the datetime module to access the built-in functions…")
import datetime

#Display the current date and time in a specific format
currdt_tm = datetime.datetime.now()
print("Current date and time:",currdt_tm.strftime("%Y-%m-%d %H:%M:%S"))
#Display the current time only
print("The Current Time is: ", currdt_tm.strftime("%H:%M:%S"))
#Display the month only
print("The Current Month is: ", currdt_tm.strftime("%m:%B"))
#Display the Weekday
print("The Current Day of the Week is: ", currdt_tm.strftime("%w:%A"))
#Display the Week of the Year
print("The Week of the Year is: ", currdt_tm.strftime("%U"))


