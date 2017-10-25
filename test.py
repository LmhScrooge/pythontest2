import datetime
import time

if __name__ == "__main__":
    times1 = datetime.datetime.now()
    time.sleep(10)
    times2 = datetime.datetime.now()
    print(times2 - times1)