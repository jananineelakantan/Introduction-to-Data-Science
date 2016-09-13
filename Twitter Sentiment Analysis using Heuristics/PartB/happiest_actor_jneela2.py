import sys
import csv
import re

def main():
    sent_file = open(sys.argv[1])                              #open the AFINN-111.txt file
    csv_file = open(sys.argv[2])                               #open breaking_bad_tweets.csv file
    file_reader = csv.reader(csv_file)        
    user_tweet = {}      
    scores = {}
    user_sentiment_score = {}

    #Form a dictionary 'scores' using data from AFINN-111.txt with each unique term as the key and sentiment score as the value
    for line in sent_file:
    	term,score = line.strip("\n").split("\t")
    	scores[term] = score 

    #Form a dictionary 'user_tweet' using data from breaking_bad_tweets_jneela2.csv with each username as the key and list of tweets as the value. 
    #Leave out the first line of the csv file while reading because that is the header line.
    for row in file_reader:    	
    	if(file_reader.line_num == 1):
    		continue    	    	
    	try:
    		user_tweet[row[0]].append(row[1])
    	except KeyError:
    		user_tweet[row[0]] = []
    		user_tweet[row[0]].append(row[1])
    
    #Clean each tweet in the list of tweets for each user
    for key,value in user_tweet.items():
    	for tweet in value:
    		tweet = re.sub('[^A-Za-z0-9\s😂😭😫😍]+', '', tweet)
    		tweet = tweet.lower()

    #Compute sentiment score for each tweet in the list of tweets for each username. Compute total number of tweets for each user.
    #Compute average sentiment score for each user.
    for key,value in user_tweet.items():    	
    	count_tweets = len(value)                                    #number of tweets for each user
    	total_sentiment_score = 0

    	for val in value:    		
    		words_list = val.split()    		
    		sentiment_score = 0
    		for word in words_list:
    			if(word in sorted(scores.keys())):
    				sentiment_score += int(scores[word])            #sentiment score for each individual tweet
    			else:
    				sentiment_score += 0    		
    		total_sentiment_score += sentiment_score    	        #total sentiment score of all tweets

    	avg_sentiment_score = total_sentiment_score/count_tweets    	
    	user_sentiment_score[key] = avg_sentiment_score    	        #dictionary with username as key and average sentiment score as value

    for key,value in sorted(user_sentiment_score.items(), key=lambda t:t[1], reverse=True):
    	line = "[" + str(value) + "]: [" + key + "]"
    	print(line)

if __name__ == '__main__':
    main()
