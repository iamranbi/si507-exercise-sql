########################
## query the database ##
########################

import sqlite3

DB_NAME='tweets.sqlite'
try:
    conn=sqlite3.connect(DB_NAME)
    cur=conn.cursor()
except Error as e:
    print(e)

# print the tweet with the most number of retweets
def get_most_retweeted_tweet():
    st_most_retweeted="SELECT TweetText FROM Tweets ORDER BY RetweetCount DESC LIMIT 1"
    cur.execute(st_most_retweeted)
    print("tweet with the most number of retweets: \n")
    for row in cur:
        print(row[0].decode('utf8'))
    print("------------------------------------------------------------")

# print the user’s screen name who is most followed
def get_most_followed_user():
    st_most_followed="SELECT ScreenName FROM Tweets ORDER BY FollowerCount DESC LIMIT 1"
    cur.execute(st_most_followed)
    print("user’s screen name who is most followed: \n")
    for row in cur:
        print(row[0])
    print("------------------------------------------------------------")

# print the user’s screen name who’s tweet had the highest retweet count
def get_most_retweeted_user():
    st_retweeted_user="SELECT ScreenName FROM Tweets ORDER BY RetweetCount DESC LIMIT 1"
    cur.execute(st_retweeted_user)
    print("user’s screen name whose tweet had the highest retweet count: \n")
    for row in cur:
        print(row[0])
    print("------------------------------------------------------------")

# print the 5 tweets that belong to authors with highest number of followers (in descending order)
def get_tweets_from_most_followed():
    st_tw_followed="SELECT TweetText FROM Tweets ORDER BY FollowerCount DESC LIMIT 5"
    cur.execute(st_tw_followed)
    print("5 tweets that belong to authors with highest number of followers: \n")
    for row in cur:
        print(row[0].decode('utf8'))
    print("------------------------------------------------------------")

# print the top 5 locations that are tweeting
def get_trending_location():
    st_location="SELECT Location FROM Tweets GROUP BY Location "
    st_location+="HAVING Location !='' ORDER BY COUNT(*) DESC LIMIT 5"
    cur.execute(st_location)
    print("top 5 locations that are tweeting: \n")
    for row in cur:
        print(row[0])
    print("------------------------------------------------------------")

get_most_retweeted_tweet()
get_tweets_from_most_followed()
get_most_followed_user()
get_most_retweeted_user()
get_trending_location()

conn.close()
