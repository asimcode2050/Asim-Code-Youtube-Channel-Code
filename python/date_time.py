
from datetime import datetime, timedelta
current_datetime = datetime.now()
print("Current datetime:", current_datetime)
some_date = datetime(2024, 11, 17)
print("Some date:", some_date.date())
new_date = current_datetime + timedelta(days=5)
print("New date (5 days later):", new_date)
earlier_date = current_datetime - timedelta(days=10)
print("Earlier date (10 days ago):", earlier_date)
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_date)
date_str = "2024-11-17 15:30:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_date)
current_time = current_datetime.time()
print("Current time:", current_time)
