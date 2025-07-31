from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time is: ", current_date)

display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter number of days: "))
    date_today= datetime.today().date()
    future_date = date_today + timedelta(days=number_of_days)
    print ("The future date will be: ", future_date)

calculate_future_date()

