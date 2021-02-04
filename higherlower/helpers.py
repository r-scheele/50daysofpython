from game_data import data
from random import randint

def test(arg, a, b):
    if arg == 'A' and a['follower_count'] > b['follower_count']:
        return 'A'
    elif arg == 'B' and b['follower_count'] > b['follower_count']:
        return 'B'

def compare():
    return data[randint(1, len(data) - 1)]