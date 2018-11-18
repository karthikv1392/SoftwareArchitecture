# Generate sensor data randonlu in time intervals of 2 seconds
# Keep generating this data

import time
from datetime import datetime
from random import *
import os

def data_generator():
    # Generate data inside the data folder
    f = open("data/sensor1.txt", "a",os.O_NONBLOCK)
    while(1):
        data = round(uniform(1, 10),2)   # Generate a value between 1 and 10
        timestamp = int(time.mktime(datetime.now().timetuple()))  # Get the current time
        text  = str(timestamp) + " " + str(data) + "\n"
        f.write(text)
        f.flush()
        time.sleep(2)



if __name__ == '__main__':
    data_generator()
