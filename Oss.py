
import datetime

today = datetime.datetime.now().strftime("%H:%M:%S")
today = str(today)
print("Hello Cron, the time is: ", today)
