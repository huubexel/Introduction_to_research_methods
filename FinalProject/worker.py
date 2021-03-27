# hier moet het dus in komen, eerst maar ff kijken hoe die pathing werkt want dat is ook wat hoor
# der moet dus nog idd komen:
# een function (bijvoorbeeld get_file die zorgt dat je elke keer de juiste file aanlevert.)

import nltk

def make_in_a_set(filepath):
    file_in_a_set = set()
    with open(filepath, 'r') as f:  # Open file for read
        for line in f:
            # I am going to make everything lower so I can check without having to worry about case sensitivity
            line = line.lower()
            line_without_newline = line.split('\n')[0]
            file_in_a_set.add(line_without_newline)
    return file_in_a_set

def check_place(north_places, south_places):

    north_matched_tweets = []
    north_counter = 0
    south_matched_tweets = []
    south_counter = 0

    with open('./Data/April/tweets_apr_01.txt', 'r') as f:  # Open file for read
        for tweet in f:
            # Place only gives you the place of every tweet on a seperate line
            place_only = tweet.split('\t')[1]
            place_only = place_only.lower()
            place_tokenized = nltk.word_tokenize(place_only)
            for possible_match in place_tokenized:
                if possible_match in north_places:
                    north_matched_tweets.append(tweet.split('\t')[0])
                    north_counter +=1
                elif possible_match in south_places:
                    south_matched_tweets.append(tweet.split('\t')[0])
                    south_counter +=1
    return (north_matched_tweets, south_matched_tweets)     


def main():
  
    # all these files have been made into sets for extra speed.
    south_places_set = make_in_a_set('./all_south_places.txt')
    north_places_set = make_in_a_set('./all_north_places.txt')
    bad_words_set = make_in_a_set('./bad_words.txt')
    good_words_set = make_in_a_set('./good_words.txt')

    north_tweets, south_tweets = check_place(north_places_set, south_places_set)    
    #check_tweet(north_tweets, south_tweets, good_words_set, bad_words_set)



if __name__ == "__main__":
    main()
