from random import uniform
from datetime import timedelta

def add_small_time_noise(timestamp):
    return timestamp + timedelta(seconds=uniform(1,60), minutes=uniform(1,20))
