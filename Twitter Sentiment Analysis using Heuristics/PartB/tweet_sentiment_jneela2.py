import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])                                   #open AFINN-111.txt
    tweet_file = open(sys.argv[2])                                  #open streaming_output_full.txt
    raw_tweet_data = []
    tweet_data = []    
    scores = {}                                                     #scores dictionary holds sentiment score for each word in AFINN-111.txt    
    tweet_sentiment = {}                                            #tweet_sentiment diciotnary holds sentiment score for each tweet 
    for line in sent_file:
    	term,score = line.strip("\n").split("\t")
    	scores[term] = score    

    #Each line in tweet_file is a string that looks like JSON. json.loads(line) parses this to dictionary.
    for line in tweet_file:
    	json_data = json.loads(line)
    	raw_tweet_data.append(json_data["text"])                     #raw_tweet_data contains list of all tweets

    for tweet in raw_tweet_data:
    	tweet = re.sub('[^A-Za-z0-9\s😂😭😫😍]+', '', tweet)
    	tweet = tweet.lower()
    	tweet_data.append(tweet)                                     #tweet_data contains tweets stripped of all special characters
    
    #Iterate through tweet_data list. Get each tweet. Split each tweet into words. For each word look up the sentiment
    #score in scores dictionary. Add up the individual sentiment scores to get the sentiment score of whole tweet.
    for tweet in tweet_data:
    	words_list = tweet.split()
    	sentiment_score = 0
    	for word in words_list:
    		if(word in sorted(scores.keys())):
    			sentiment_score += int(scores[word])
    		else:
    			sentiment_score += 0

    	try:
    		tweet_sentiment[tweet] = sentiment_score
    	except KeyError:
    		tweet_sentiment[tweet] = sentiment_score

    #Sort tweet_sentiment in reverse order based on values and take the first 10 values
    for key,value in sorted(tweet_sentiment.items(), key=lambda t:t[1], reverse = True)[:10]:
    	line = "[" + str(value) + "]: [" + key + "]"
    	print(line)    
    
    #Sort tweet_sentiment in reverse order based on values and take the bottom 10 values
    #for key,value in sorted(tweet_sentiment.items(), key=lambda t:t[1], reverse = True)[-11:-1]:
    for key,value in sorted(tweet_sentiment.items(), key=lambda t:t[1], reverse = True)[-10:]:
    	line = "[" + str(value) + "]: [" + key + "]"
    	print(line)

if __name__ == '__main__':
    main()
