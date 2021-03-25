# hier moet het dus in komen, eerst maar ff kijken hoe die pathing werkt want dat is ook wat hoor






def make_in_a_set(filepath):
    file_in_a_set = set()
    with open(filepath, 'r') as f:  # Open file for read
        for line in f:
            line_without_newline = line.split('\n')[0]
            file_in_a_set.add(line_without_newline)
    return file_in_a_set




def main():
    south_places_file_path = './all_south_places.txt'
    north_places_file_path = './all_north_places.txt'
    bad_words_file_path = './bad_words.txt'
    good_words_file_path = './good_words.txt'
    
    
    south_places_set = make_in_a_set(south_places_file_path)
    north_places_set = make_in_a_set(north_places_file_path)
    bad_words_set = make_in_a_set(bad_words_file_path)
    good_words_set = make_in_a_set(good_words_file_path)



    #with open('./Data/April/tweets_apr_01.txt', 'r') as f:  # Open file for read
        #for line in f:
            # nu kun je hier zegmaar iets doen met de tweets, 
            # ik weet hoe graag je wil regelen dat het systeem nu goed loopt maar,
            # het is belangrijker om eerst te regelen dat we nu iets gaan doen met een line.





if __name__ == "__main__":
    main()
