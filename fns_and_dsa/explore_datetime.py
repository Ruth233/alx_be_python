from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days into the future: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print("The date after", days, "days will be:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer number of days.")

# Run the functions
display_current_datetime()
calculate_future_date()