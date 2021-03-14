# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import tweepy
import os
import random
import datetime

tweetlist = r" tweet_list_dir "

tweet_log = r" randomtweet_log.txt "

timenow = datetime.datetime.now().strftime("%Y%m%d_%H%M")

consumer_key = ' consumer key '
consumer_secret = ' consumer secret '
access_token = ' access token '
access_token_secret = ' access token secret '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


# -

def main():
    
    filelist = []
    
    for f in os.listdir(tweetlist):
        if not f.startswith("."):
            filelist.append(f)
            
    tweet = random.choice(filelist)
    
    print(tweet)
    
    with open(tweet_log, "a") as log_out:
        log_out.write(timenow + ", " + tweet + "\n")
    
    with open(tweetlist + "/" + tweet, "r") as file:
        tweet_content = file.read()
        
        api.update_status(tweet_content)


if __name__ == '__main__':
    main()




