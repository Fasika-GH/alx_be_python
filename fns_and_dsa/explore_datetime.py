from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted)

display_current_datetime()

def calculate_future_date():
    number_of_days = input("Enter number of days to add to the current date:")
    date_today= datetime.today().date()
    future_date = date_today + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print ("The future date will be: ", formatted_future_date)

calculate_future_date()

