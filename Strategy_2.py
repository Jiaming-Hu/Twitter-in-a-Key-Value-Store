import redis
from Abstract_strategy import strategy

class strategy_2(strategy):

    def insert_follower(self, user_id, follow_id): # user of user_id follows the user with follow_id

        # eg : user_1_followed_by : [user3, ..., usern]
        self.r.sadd('user_' + str(follow_id) + '_followed_by', user_id)

    def insert_tweet(self, user_id, tweet_text):

        tweet_id = self.r.incr("tweet_id", 1)

        # connect tweet_id (key) with tweet_text
        self.r.set('tweet_' + str(tweet_id) + '_tweet_text', tweet_text)

        # add tweet to user's followers' timeline
        # get list of users that follows this user
        followers = self.r.smembers('user_' + str(user_id) + '_followed_by')

        for u_id in followers: # update all followers' timeline

            # update timeline of the user
            self.r.lpush('user_' + str(u_id) + "_timeline", tweet_id)

    def get_timeline(self, user_id):

        # initialize the result
        ten_most_recent_tweet = []

        # get all the tweet_id of the tweet in this user's timeline
        # get the 10 most recent (already sorted by timeline reverse)
        ten_most_recent_tweet_id = self.r.lrange('user_' + str(user_id) + '_timeline', 0, 9)

        # You can uncomment the next line to see the sorted ten tweet_id
        # print(ten_most_recent_tweet_id)

        for t_id in ten_most_recent_tweet_id: # transform tweet_id to tweet_text

            ten_most_recent_tweet.append(self.r.get('tweet_' + str(t_id) + "_tweet_text"))

        # You can uncomment the next line to see the tweet_text
        # print(ten_most_recent_tweet)

        return ten_most_recent_tweet
