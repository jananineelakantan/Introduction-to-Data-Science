import sys
import json
import re

def main():
    tweet_file = open(sys.argv[2])    
    stopword_file = open(sys.argv[1])
    #TODO: Implement
    tweet_data = []
    clean_tweet_data = []
    full_tweet_list = []
    stopword_list = []
    term_occurence = {}
    term_frequency = {}

    for line in stopword_file:
    	stopword_list.append(line.strip())                         #form a list of stop words

    #Each line in tweet_file is a string that looks like JSON. json.loads(line) parses this to dictionary.
    for line in tweet_file:
    	json_data = json.loads(line)
    	tweet_data.append(json_data["text"])                        #tweet_data contains list of all tweets

    for tweet in tweet_data:
    	tweet = re.sub('[^A-Za-z0-9\s]+', '', tweet)
    	tweet = tweet.lower()
    	clean_tweet_data.append(tweet)                              #clean_tweet_data contains tweets stripped of all special characters
    
    for tweet in clean_tweet_data:
    	words_list = tweet.split()                                  #get all the words in a tweet sentence. words_list is a list of tweet words.
    	for word in words_list:
    		if(word not in stopword_list):
    			full_tweet_list.append(word)                        #form a list of only those words that are not part of stopword list

    #Form a dictionary of <term,# of occurrences>
    for word in full_tweet_list:
    	try:
    		term_occurence[word] += 1                               #form a dictionary with term as the key and no of occurences as the value
    	except KeyError:
    		term_occurence[word] = 1

    total_occurrences = sum(term_occurence.values())                #calculate total occurrences of all words in all tweets

    for key,value in term_occurence.items():
    	 occ = value/total_occurrences                              #calculate term frequency for each term and round off to 5 decimal places
    	 term_frequency[key] = round(occ,5)                         #form a dictionary with term as the key and term freq as the value

    # with open('term_freq_jneela2.txt','w') as f:
    # 	line = "[term] [frequency]\n"
    # 	f.write(line)
    print("[term] [frequency]")
    for key,value in sorted(term_frequency.items(), key = lambda t:t[1], reverse = True):       #Print terms with their term freq in descending order. Most frequent term appears at the top.
        line = key + " " + str(value)
        print(line)

if __name__ == '__main__':
    main()
