import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])                                  #open AFINN-111.txt file
    tweet_file = open(sys.argv[2])                                 #open streaming_output_full.txt
    location_file = open("states_abbr.txt")                        #open states_abbr.txt file
    scores = {}
    all_tweets_location = []                                       #List with dictionary of values in the form {"tweet":<text of tweet>,"location":<location>}
    state = {}  
    statewise_tweet = {}
    state_sentiment_score = {}
    
    #Create a dictionary with state abbreviation as the key and its full name as value. Only US states are considered.
    for line in location_file:
    	line = line.strip(",").strip("\n")
    	line = re.sub('\"','',line)
    	state_abbr,state_descr = line.split(":")
    	state[state_abbr.lower()] = state_descr.lower()
    
    #Create a dictionary with term as key and its sentiment score as value
    for line in sent_file:
    	term,score = line.strip("\n").split("\t")
    	scores[term] = score  

    #Each line in tweet_file is a string that looks like JSON. json.loads(line) parses this to dictionary.
    for line in tweet_file:
    	json_data = json.loads(line)
    	each_tweet_loc = {}
    	each_tweet_loc["tweet"] = json_data["text"]                              #Extract tweet text and location information from each tweet in the dictionary
    	each_tweet_loc["location"] = json_data["user"]["location"]    	         #each_tweet_loc is a dictionary with tweet and location as the keys
    	all_tweets_location.append(each_tweet_loc)                               #List of dictionaries
    
    
    #Location could be a valid location or any string of words. Clean the location data.Split it into list of words.
    #Find if any word in the location matches either the key or the value in the states dictionary.
    #For the matching location, put it into statewise_tweet dictionary as the key. List of tweets for this location form the value.
    for list_dict in all_tweets_location:    	  	
    	if(type(list_dict["location"]) is str):    		
    		loc = re.sub('[^A-Za-z0-9\s]+', '', list_dict["location"])
    		loc = loc.lower()
    		word_list = loc.split()

    		key1 = ""
    		
    		for word in word_list:
    			if(word in state.keys()):
    				key1 = word
    				break
    			else:
    				for key,val in state.items():
    					if(word == val):
    						key1 = key
    						break

    		#Create a dictionary with state abbr as key and list of tweets as value
    		if(key1 != ""):
    			try:
    				statewise_tweet[key1].append(list_dict["tweet"])
    			except KeyError:
    				statewise_tweet[key1] = []
    				statewise_tweet[key1].append(list_dict["tweet"])

    #Clean each tweet in the list of tweets for each state
    for key,value in statewise_tweet.items():  
    	for tweet in value:
    		tweet = re.sub('[^A-Za-z0-9\s😂😭😫😍]+', '', tweet)
    		tweet = tweet.lower()

    #Compute sentiment score for each tweet in the list of tweets for each state
    #Compute average sentiment score for each state
    for key,value in statewise_tweet.items():    	
    	count_tweets = len(value)
    	total_sentiment_score = 0

    	for val in value:    		
    		words_list = val.split()    		
    		sentiment_score = 0
    		for word in words_list:
    			if(word in sorted(scores)):
    				sentiment_score += int(scores[word])
    			else:
    				sentiment_score += 0    		
    		total_sentiment_score += sentiment_score    	

    	avg_sentiment_score = total_sentiment_score/count_tweets    	
    	state_sentiment_score[key] = avg_sentiment_score    	

    for key,value in sorted(state_sentiment_score.items(), key=lambda t:t[1], reverse=True):
    	line = "[" + str(value) + "]: [" + key.upper() + "]"
    	print(line)    

if __name__ == '__main__':
    main()
