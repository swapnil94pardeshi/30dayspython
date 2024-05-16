from datetime import datetime

print(dir(datetime))
now=datetime.now()
print(now)

new_year = datetime(2020, 1, 1)

print(new_year.day)
print(new_year.month)
print(new_year.year)
print(new_year.second)
print(new_year.minute)
print(new_year.hour)


#Get the current day, month, year, hour, minute and timestamp from datetime module

current_date=datetime.now()
print(current_date)

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(current_date.strftime("%m/%d/%Y, %H:%M:%S"))

#Today is 5 December, 2019. Change this time string to time.

date_string="5 December, 2019"
print(datetime.strptime(date_string,"%d %B, %Y"))

#Calculate the time difference between now and new year.
new_year=datetime(2025,1,1)
print(new_year-current_date)

#Calculate the time difference between 1 January 1970 and now.

datetocal=("1 January 1970")
print(current_date-(datetime.strptime(datetocal,"%d %B %Y")))

