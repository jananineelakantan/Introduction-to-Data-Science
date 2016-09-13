******************HOMEWORK 3 PART B*************************

Name: Janani Neelakantan
UIN : 670805407
ID  : jneela2

The folder Part B contains the following files:
1)README_jneela2.txt
2)tweet_sentiment_jneela2.py - Python code to compute sentiment score for each tweet
3)happiest_actor_jneela2.py - Python code to compute average sentiment score for each actor
4)happiest_state_jneela2.py - Python code to compute average sentiment score for each state in the US
5)reportb_jneela2.txt
6)AFINN-111.txt - File with precomputed sentiment scores for each word. Added few words and emoticons of my choice. 
7)states_abbr.txt - File with list of state abbreviations and their full names

Please use the following commands for each section:

SENTIMENT OF EACH TWEET
python3 tweet_sentiment_jneela2.py ~/hw3/data/AFINN-111.txt streaming_output_full.txt > tweet_sentiment_jneela2.txt

HAPPIEST BREAKING BAD ACTOR
python3 happiest_actor_jneela2.py ~/hw3/data/AFINN-111.txt breaking_bad_tweets_jneela2.csv > happiest_actor_jneela2.txt

HAPPIEST STATE
python3 happiest_state_jneela2.py ~/hw3/data/AFINN-111.txt streaming_output_full.txt > happiest_state_jneela2.txt
