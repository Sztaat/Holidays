from datetime import datetime, timedelta
 
date1 = input('Enter beggining date - DD/MM/YYYY: ')
date2 = input('Enter ending date - DD/MM/YYYY: ')
format =  '%d/%m/%Y'
 
delta = (datetime.strptime(date2, format)-datetime.strptime(date1, format))

x = 0.0767123
result = round(x * delta.days, 2)
    
print("Holiday entitlement:", result, "days")
input()