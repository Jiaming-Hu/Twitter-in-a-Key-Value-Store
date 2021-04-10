from Strategy_1 import strategy_1
from Strategy_2 import strategy_2
from Abstract_strategy import strategy
import time
import pandas as pd

# load data with selected strategy
def load_data(strategy):
    load_follow(strategy)
    load_tweet(strategy)

# load follow relation data
def load_follow(strategy):

    follow_num = 0

    # read in data
    follow_df = pd.read_csv("follower.csv", sep = "\t").set_index("index")
    follow_row_num = len(follow_df.index)

    # choose api
    if strategy == 1:
        load_follow_help(strategy_1(), follow_df, follow_row_num)
    else:
        load_follow_help(strategy_2(), follow_df, follow_row_num)


def load_follow_help(db, follow_df, follow_row_num):

    total_time = 0
    follow_num = 0

    # load follow data
    for i in range(follow_row_num):

        row = [str(item) for item in list(follow_df.iloc[i])]
        user_id = row[0]
        follows_id = row[1]

        start = time.time()
        db.insert_follower(user_id, follows_id)
        total_time += time.time() - start

        follow_num += 1
        print(follow_num)

    print('Time used to load ', follow_num, 'follow is:', total_time, 'seconds.')


def load_tweet(strategy):

    tweet_num = 0

    tweet_df = pd.read_csv("tweet.csv", sep = "\t").set_index("index")

    # sort the tweet by timestamp
    tweet_df = tweet_df.sort_values(by = ['tweet_ts'])

    tweet_row_num = len(tweet_df.index)

    if strategy == 1:
        load_tweet_help(strategy_1(), tweet_df, tweet_row_num)
    else:
        load_tweet_help(strategy_2(), tweet_df, tweet_row_num)

def load_tweet_help(db, tweet_df, tweet_row_num):

    total_time = 0
    tweet_num = 0

    for i in range(tweet_row_num):
        row = [str(item) for item in list(tweet_df.iloc[i])]
        user_id = row[1]
        tweet_text = row[3]

        start = time.time()
        db.insert_tweet(user_id, tweet_text)
        total_time += time.time() - start

        tweet_num += 1

    print('Time used to load ', tweet_num, 'tweets is:', total_time, 'seconds.')

if __name__ == '__main__':

    load_data(1)
    load_data(2)
