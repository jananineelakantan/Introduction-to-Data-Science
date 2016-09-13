import argparse
import oauth2 as oauth
import urllib.request as urllib
import json
import sys
import csv

# See Assignment 1 instructions for how to get these credentials
access_token_key = "706749031909875712-75ze2NBc5TrosebCFTkUUrRcAcGbhuT"
access_token_secret = "yO4hte1LHZ6gE66LLbnkKeVc2C2sIYoZenkhmy6B0CbY5"

consumer_key = "EXku17HdpZBAwup1LxXwUNHCj"
consumer_secret = "hOJmT0hSb6eLKecSdgJy0KaAdWLef5aR29Xpd012PIoqBCGxAF"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

#Fetch sample of current Twitter stream. The statement line.strip().decode('utf-8') is required to remove unreadable characters.
def fetch_samples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print (line.strip().decode('utf-8'))

#Fetch sample of tweet data for the given term. Specifying ("count",100) gives 100 tweets for the term.
def fetch_by_terms(term):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    parameters = [("q", term),("count", 100)]
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print (line.strip().decode('utf-8'))

def fetch_by_user_names(user_name_file):
    #Fetch the tweets by the list of usernames and write them to stdout in the CSV format
    sn_file = open(user_name_file)								   #Open the user_names.txt file
    result_file = csv.writer(open("breaking_bad_tweets_jneela2.csv","w"))
    result_file.writerow(["user_name", "tweet"])  
    name = []
    for line in sn_file:
        name.append(line.strip('\n'))                              #All the names are put into a list
    for nm in name:
        tweet = []
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        parameters = [("screen_name", nm),("count", 100)]
        response = twitterreq(url, "GET", parameters)              #response contains multiple json objects               
        for ln in response:                                        #iterate through response to get each json object
        	json_data = json.loads(ln.strip().decode('utf-8'))     #json_data is now a list of dictionaries
        	for data in json_data:                                 #json_data may contain at the max 100 dictionaries
        		for key in data:                                   #For each dict iterate through the keys to get 'text' key                  
        			if(key == 'text'):
        				tweet.append(data[key])                    #Put all the tweet texts into a list. Could be used later.
        				result_file.writerow([nm,data[key]])
        #result_file.writerow([nm,tweet])
 
        #writer = csv.writer(sys.stdout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Enter the command')
    parser.add_argument('-term', help='Enter the search term')
    parser.add_argument('-file', help='Enter the user name file')
    opts = parser.parse_args()
    if opts.c == "fetch_samples":
        fetch_samples()
    elif opts.c == "fetch_by_terms":
        term = opts.term
        print (term)
        fetch_by_terms(term)
    elif opts.c == "fetch_by_user_names":
        user_name_file = opts.file
        fetch_by_user_names(user_name_file)
    else:
        raise Exception("Unrecognized command")
