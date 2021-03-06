# Things you have to consider is that if the data is
# from 2008, 2012, 2016, 2020 etc. than that data is from a leap year.
# For this python code to work, you have to make it so the amount
# that you put into the loop in the range(amount) part (in file_path_handler),
# is the same as the amount of days in that month.
# I am using data from the year 2018 which is not a leap year,
# so I can put 28 in as the amount for the data that I am using.
# But if you are using data from say (only) 2016,
# than you have to make sure that you take the leap year into account and put 29 as the amount.

# Imports the tokenizer
import nltk

def file_path_handler():
# This function makes all the possible filepaths for the data and puts them 
# in 1 list in order to handle them better later on

    # This is the list were all the file paths will go in
    file_paths = []
    
    # January file paths (31 days)
    for i in range(31):
        flexible_filepath = "./Data/{0}/tweets_{1}_{2}.txt".format("January", "jan", (i + 1))
        file_paths.append(flexible_filepath)
        
    # February file paths (28 days, 2018 = no leap year)   
    for i in range(28):
        flexible_filepath = "./Data/{0}/tweets_{1}_{2}.txt".format("February", "feb", (i + 1))
        file_paths.append(flexible_filepath)

    # March file paths (31 days)
    for i in range(31):
        flexible_filepath = "./Data/{0}/tweets_{1}_{2}.txt".format("March", "mar", (i + 1))
        file_paths.append(flexible_filepath)

    # April file paths (30 days)
    for i in range(30):
        flexible_filepath = "./Data/{0}/tweets_{1}_{2}.txt".format("April", "apr", (i + 1))
        file_paths.append(flexible_filepath)
        
    return file_paths        

def make_in_a_set(filepath):
    # This function puts files into a faster and better usable set

    file_in_a_set = set() 					# creates the set
    with open(filepath, 'r') as f:  				# Open file for read
        for line in f:						# for every line in that file
            line = line.lower()				# making everything lower so it is easier to work with
            line_without_newline = line.split('\n')[0]	# Removes the newline from every line
            file_in_a_set.add(line_without_newline)		# adds the line to the set
    return file_in_a_set					# return the set

def check_place(north_places, south_places, filepath):
# This function checks whether tweets are send by people that live in the 
# north or the south of the Netherlands and saves those tweets for later
# use in two seperate lists.

    # In these two lists will the tweets go that matched with
    # either places in the north- or in the south of the Netherlands
    north_matched_tweets = []
    south_matched_tweets = []

    # Opens the file
    with open(filepath, 'r') as f:  	# Open file for read
        for tweet in f:
        
            # place_only gives you the place of every tweet on a seperate line
            place_only = tweet.split('\t')[1]
            
            # lower() makes them compatible with the other sets
            place_only = place_only.lower()
            
            # Tokenizes what people filled into their account as the place
            # This because most of the people fill in something like this:
            # Groningen,Nederland   which would not get Groningen 
            # (which is a place in the North of the Netherlands)
            place_tokenized = nltk.word_tokenize(place_only)
            
            # for every seperate word of what people filled in into their 
            # living place check if that place is in the north or south
            # if that is the case than append that tweet to the list that it belongs to.
            for possible_match in place_tokenized:
                if possible_match in north_places:
                    north_matched_tweets.append(tweet.split('\t')[0])
                    
                elif possible_match in south_places:
                    south_matched_tweets.append(tweet.split('\t')[0])
                    
    # return the tweets that matched with north and tweets that matched with the south
    return (north_matched_tweets, south_matched_tweets)     


def tweet_tokenizer(tweets):
    # this function tokenizes the tweets which makes them more usable later on.
    tokenized_tweets = []
    for tweet in tweets:
        tweet = nltk.word_tokenize(tweet)
        tokenized_tweets.append(tweet)
    return tokenized_tweets

def check_emotion(tweets, bad_words, good_words):
# This function checks if there are any good or bad words in the tweets.
# If there are as many good words as bad words in one tweet than it is not considered
# either a good or bad tweet. If there are for example two good words and one bad word
# than the tweet is considered good cause there are more good words in the tweet than bad words.

    # These two count the total good tweets and bad tweets
    good_tweets = 0
    bad_tweets = 0
    
    for tweet in tweets:
        positive_words = 0	# positive word counter per tweet
        negative_words = 0 	# negative word counter per tweet
        
        for word in tweet:
            if word in good_words:
                positive_words +=1      	# if the word is in the positive list than its considered a positive word
            elif word in bad_words:
                negative_words +=1		# if the word is in the negative list than its considered a negative word
                      
        # If there are more positive words in a tweet than negative words than the tweet is considered a positive tweet              
        if positive_words > negative_words: 		
            good_tweets +=1
            
        # If there are more negative words in a tweet than positive words than the tweet is considered a negative tweet    
        elif negative_words > positive_words:
            bad_tweets +=1
    
    # returns how many good and how many bad tweets        
    return (good_tweets, bad_tweets)
    

def main():
  
    # these four are the total counters, so they count the numbers that we want to know in the end.
    total_good_tweets_north = 0
    total_bad_tweets_north = 0
    total_good_tweets_south = 0
    total_bad_tweets_south = 0
    
    # all these files have been made into sets for extra speed.
    south_places_set = make_in_a_set('./all_south_places.txt')
    north_places_set = make_in_a_set('./all_north_places.txt')
    bad_words_set = make_in_a_set('./bad_words.txt')
    good_words_set = make_in_a_set('./good_words.txt')
    
    # all the file paths needed are made here
    file_paths = file_path_handler()

    # for every day of the first four months of 2018 do the following:
    for i in range(31 + 28 + 31 + 30):
    
        # checks if the tweets come out of the north or south of the Netherlands
        # (or from a different place but those are not saved in any way) and saves that in seperate variables
        north_tweets, south_tweets = check_place(north_places_set, south_places_set, file_paths[i])
    
        # tokenizes tweets
        north_tokenized = tweet_tokenizer(north_tweets)
        south_tokenized = tweet_tokenizer(south_tweets)
    
        # checks tweets in the north if they are good or bad (or neither, but those are not saved in any way)
        # and saves those amounts in seperate variables
        good_tweets_north_counted, bad_tweets_north_counted = check_emotion(north_tokenized, bad_words_set, good_words_set)

        # adds the total amount of good and bad tweets from the north to the total variables
        total_good_tweets_north = total_good_tweets_north + good_tweets_north_counted
        total_bad_tweets_north = total_bad_tweets_north + bad_tweets_north_counted

        # checks tweets in the south if they are good or bad (or neither, but those are not saved in any way)
        # and saves those amounts in seperate variables
        good_tweets_south_counted, bad_tweets_south_counted = check_emotion(south_tokenized, bad_words_set, good_words_set)
                
        # adds the total amount of good and bad tweets from the south to the total variables        
        total_good_tweets_south = total_good_tweets_south + good_tweets_south_counted
        total_bad_tweets_south = total_bad_tweets_south + bad_tweets_south_counted
        
    print("The total amount of good tweets that were tweeted in the first 4 months of 2018 in the North of the netherlands is: {0}".format(total_good_tweets_north))
    print("The total amount of bad tweets that were tweeted in the first 4 months of 2018 in the North of the netherlands is: {0}".format(total_bad_tweets_north))
    print("The total amount of good tweets that were tweeted in the first 4 months of 2018 in the South of the netherlands is: {0}".format(total_good_tweets_south))
    print("The total amount of bad tweets that were tweeted in the first 4 months of 2018 in the South of the netherlands is: {0}".format(total_bad_tweets_south))


if __name__ == "__main__":
    main()
