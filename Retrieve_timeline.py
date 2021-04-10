from Strategy_1 import strategy_1
from Strategy_2 import strategy_2
from Abstract_strategy import strategy
import time
import random

# retrieve timeline based on strategy number
def retrieve_timelines(strategy):

    # choose api
    if strategy == 1:
        db = strategy_1()
    else:
        db = strategy_2()

    # run 1 minutes
    end = time.time() + 60
    # initialize the result
    retrieved_timeline_num = 0

    while time.time() < end:

        # randomly choose a user from ten Thousand Users
        user_id = random.randint(1000001, 1010000)

        db.get_timeline(user_id)

        retrieved_timeline_num += 1

    print("Number of timlines retrieved in one minute: ", retrieved_timeline_num)

if __name__ == '__main__':
    retrieve_timelines(1)
    retrieve_timelines(2)
