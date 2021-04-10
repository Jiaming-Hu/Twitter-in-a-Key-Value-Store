# Twitter-in-a-Key-Value-Store

## Description
You built an application to pump up to 1 million tweets into a database and to retrieve home timelines for random users. 
Probably you discovered that there are many factors that impact tweet insertions performance and that retrieving home timelines using
a JOIN query is especially slow. Twitter recognized that a relational approach would not scale with their growth and migrated their business
to a scalable NoSQL-based approach using Redis.

I will reuse the tweets and follower-followee datasets but now re- implement your API to use Redis instead of a Relational database.


## There are two strategies I would explore for the Redis-based implementation:


### Redis Strategy 1: 
When you post a tweet, it is a simple addition of a key and a value and should be very fast! 
But the getTimeline operation would now require that you look up the tweets of each of your followers, 
constructing the home timeline on the fly and on demand.

### Redis Strategy 2: 
As you post each tweet, you broadcast the tweet (or the name of the key for the tweet) to the user’s home timeline automatically. 
This is actually what twitter does! Your write performance should be lower, but since the timeline is now ready and waiting, 
getTimeline should be a much faster operation. Let’s find out how much faster.
