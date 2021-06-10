# this file is just for following along with the videos
import os
import time
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("Path does not exist.")
    time.sleep(10)
