import datetime 

current_date = datetime.datetime.now()
print(current_date)

number_of_days = int(input("Enter the number of days to add to the current date: "))
future_date = current_date + datetime.timedelta(days=number_of_days)
print(f"Future date : {future_date}")