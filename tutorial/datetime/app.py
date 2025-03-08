from flask import Flask
from flask_cors import CORS
import datetime, time

app = Flask(__name__)
CORS(app)



# 🐍🐍🐍🐍 TIME MODULE:


# curent_time = time.time() # give current time in seconds
# print(curent_time)
# current_time_using_ctime = time.ctime() #takes by default epoch but you can pass seconds like this time.ctime([seconds])
# print(current_time_using_ctime)

# 🐍🐍🐍🐍 timestamp

# current_time = time.time() # give current epoch time or you can pass the timestamp there
# get_current_timestamp = datetime.date.fromtimestamp(current_time) # give current date according to provided timestamp
# print(get_current_timestamp)

# 🐍🐍🐍🐍 gettime() and localtime():000 
# get_time = time.gmtime() # return time in utc timezone
# print(get_time) # output: time.struct_time(tm_year=2025, tm_mon=3, tm_mday=8, tm_hour=13, tm_min=16, tm_sec=0, tm_wday=5, tm_yday=67, tm_isdst=0)
# print(get_time.tm_year) # if you want year only then use output
# local_time = time.localtime() # return local time means inidan time
# print(local_time) # output: time.struct_time(tm_year=2025, tm_mon=3, tm_mday=8, tm_hour=18, tm_min=48, tm_sec=13, tm_wday=5, tm_yday=67, tm_isdst=0)
# print(local_time.tm_mday) # same for the local time as well





# 🐍🐍🐍🐍 DATETIME MODULE:


# 🐍🐍🐍🐍 datetime_obj = datetime.datetime(2023,2,3,3,2,4)
# 🐍🐍🐍🐍datetime_obj = datetime.datetime(year=2023,month=2,day=3,hour=3,minute=2,second=4) #if you give argument for one of them then you need to put the argument for all of them and in that case order does'nt metter
# print(datetime_obj)

# 🐍🐍🐍🐍 access date and time together in %Y/%m/%d %H:%M:%S format
# current_datetime = datetime.datetime.now()
# print(current_datetime)


# 🐍🐍🐍🐍 access only time
# current_time = datetime.datetime.now().time()
# print(current_time)


# 🐍🐍🐍🐍 access date only
# current_date = datetime.datetime.now().date()
# print(current_date)

# 🐍🐍🐍🐍 here you can access the year month, day ot time individually
# access_datetime = datetime.datetime.now()
# print("year:",access_datetime.year)
# print("month:",access_datetime.month)
# print("day:",access_datetime.day)
# print("hour:",access_datetime.hour)
# print("minute:",access_datetime.minute)
# print("second:",access_datetime.second)

# 🐍🐍🐍🐍
# CODE	    MEANING	                            EXAMPLE

# %Y	    Year (4 digits)	                    2024
# %m	    Month (01-12)	                    03
# %d	    Day of the month (01-31)	        07
# %H	    Hour (00-23) (24-hour clock)        14
# %M	    Minute (00-59)	                    30
# %S	    Second (00-59)	                    45
# %I	    Hour (01-12) (12-hour clock)        02
# %p	    AM or PM	                        PM
# %a	    Weekday (abbreviated)	            Thu
# %A	    Weekday (full)	                    Thursday
# %b	    Month (abbreviated)	                Mar
# %B	    Month (full)	                    March

# 🐍🐍🐍🐍 strftime

# datetime_obj = datetime.datetime.now() # give you current date and time 
# date_fromat = datetime_obj.strftime("%Y-%m-%d")
# time_fromat = datetime_obj.strftime("%H:%M:%S")
# print(date_fromat)
# print(time_fromat)

# 🐍🐍🐍🐍 strptime

# String representing a date and time
# date_string = "2024/03/07 14:30:45"

# datetime_obj = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S -%p -%a")
# # Convert the string to a datetime object
# datetime_strp_obj = datetime.datetime.strptime(date_string, "%Y/%m/%d %H:%M:%S") # takes two args and first argument take date string and second argument take datetime format and they should be same 

# print(datetime_obj)
# print(datetime_strp_obj)
# print(type(datetime_obj)) 

# 🐍🐍🐍🐍 timestamp: 

# current_time = time.time() # give current epoch time
# get_current_timestamp = datetime.date.fromtimestamp(current_time)
# print(get_current_timestamp)




# 🐍🐍🐍🐍 TIMEDELTA MODULE:
#  (in one word it is used for time conversions) in timedelta you can add these things but here you can see that we can not update or set the date here because it is complecated to manage things 
# if developers add the years here so because of leap year it decrese the performance of timedelta object that's why for the year updatation we have oter other module called python-dateutil
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )


# today_obj = datetime.date.today()

# delta = datetime.timedelta(weeks=3) # here you can add the weeks using timedelta
# print(today_obj + delta)


# birthdate = datetime.datetime(2000,12,19)
# current = datetime.datetime.now()
# print("date:",current - birthdate)
# print("hours:",(current - birthdate)/datetime.timedelta(hours=1))
# print("minutes:",(current - birthdate)/datetime.timedelta(minutes=1))
# print("seconds:",(current - birthdate)/datetime.timedelta(seconds=1))


# run flask server
if __name__ == "__main__":
    app.run(debug=True, port=5000)