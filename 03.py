import datetime as datetime
import time

for i in range(5):
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    time_format = "%Y-%m-%d %H:%M:%S"
    print(f"{now:{time_format}}")
    time.sleep(1)