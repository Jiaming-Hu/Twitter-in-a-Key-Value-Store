import redis
from Abstract_strategy import strategy

class strategy_1(strategy):

    def insert_follower(self, user_id, follow_id): # user of user_id follows the user with follow_id

        # eg : user_1_follows : [user2, ..., usern]
        self.r.sadd('user_' + str(user_id) + '_follows', follow_id)


    # no need to insert timestamps, since they are sorted before inserting
    # tweet_id autoincreases, a tweet a latter timeline has larger tweet_id
    def insert_tweet(self, user_id, tweet_text):

        # autoincrease tweet_id
        tweet_id = self.r.incr("tweet_id", 1)

        # connect tweet_id (key) with tweet_text
        self.r.set('tweet_' + str(tweet_id) + '_tweet_text', tweet_text)

        # relate user_id (key) and the tweet_id. (A user can post multiple tweets)
        self.r.lpush('user_' + str(user_id) + "_tweets", tweet_id)

    def get_timeline(self, user_id):

        list_of_tweet_id = []

        # iniitialize the result
        recent_timeline = []

        # get all the user_id that in this user's follow
        following_list = list(self.r.smembers('user_' + str(user_id) + '_follows'))

        for user in following_list:

            # get all tweets_id of one use that's followed
            list_of_tweet_id += list(self.r.lrange('user_' + str(user) + "_tweets", 0, -1))

            # sort by tweet_id, reverse
            list_of_tweet_id.sort(reverse = True)
            # get 10 most recent tweet id
            ten_most_recent_tweet_id = list_of_tweet_id[0 : 10]

            for id in ten_most_recent_tweet_id:

                # transfer tweet to tweet_text
                recent_timeline.append(self.r.get('tweet_' + str(id) + "_tweet_text"))

        # You can uncomment the next line to see the tweet_text
        # print(recent_timeline)

        return recent_timeline
