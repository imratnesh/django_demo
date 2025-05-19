# sample/utils.py
import datetime


def fetch_current_time():
    print("fetch_current_time")
    current_time = datetime.datetime.now()
    print(f"Current time: {current_time}")
    return current_time
