# This line makes argv possible.
from sys import *

# This line makes it possible to use regex
import re

def get_input():
    # gets the filename of the textfile with all the places in them.
    textfile_input = argv[1]
    
    # opens the file and reads every string seperatly.
    with open(textfile_input, 'r') as file:
        data = file.readlines()
        
    # returns all the data   
    return data

def write_to_North(North):
    # this function appends all northern places in the (just created) all_north_places textfile
    n = open("all_north_places.txt", "a")
    for place in North:
        n.write(place + "\n")
    n.close()

def write_to_South(South):
    # this function appends all southern places in the (just created) all_south_places textfile
    s = open("all_south_places.txt", "a")
    for place in South:
        s.write(place + "\n")
    s.close()
    
def devide_North_South(textfile):

    # The list where every Northern place will be in at the end of the function
    North = []
    
    # The list where every Southern place will be in at the end of the function
    South = []
    
    # Loop through all the places of the Netherlands.
    for line in textfile:
    
    # I had to do it like this, I don't know why the "or" method did not work but it didn't,
    # so that's why all these lines are here.
        # These lines append the North lines to the North list
        # so they make sure that everything that is North in The Netherlands gets placed in one list.
        if "Groningen" in line:
            North.append(line)
        elif "Fryslân" in line:
            North.append(line)
        elif "Drenthe" in line:
            North.append(line)
    
        # These lines append the South lines to the South list
        # so they make sure that everything that is South in The Netherlands gets placed in one list.
        elif "Zeeland" in line:
            South.append(line)
        elif "Noord-Brabant" in line:
            South.append(line)
        elif "Limburg" in line:
            South.append(line)
            
        # Almost every place in Fryslân has a second Frisian name which does not say that it is in Fryslân, 
        # however, only those lines contain an "/" so if the line has a "/" in it, it is automatically Fries.
        # This line puts every Frisian name of a place to the North list.
        elif "/" in line:
            North.append(line)
    # Returnes the lists with all the Northern and all the Southern places in the Netherlands.        
    return(North, South)

def clean_line(North_or_South):
    # This function gets rid of the zipcode at the front of sentence if there is any
    revisioned_North_or_South = []
    for place in North_or_South:
        if re.match('^[0-9]*$', place[0]):
            revisioned_North_or_South.append(place[5:])
        else:
            revisioned_North_or_South.append(place)   
    return revisioned_North_or_South           
                
def only_place_name(n_or_s):

    # every line has 2 ways to start:
    # placename tab rest of the sentence
    # or 
    # Frisian placename space slash
    
    # This function makes sure that you only get the placename and not the rest of the sentence
    
    only_place_list = []
    for place in n_or_s:
        if '/' in place:
            only_place = place.split('/')[0]
            only_place_list.append(only_place)
        else:
            only_place = place.split('\t')[0]
            only_place_list.append(only_place)
    
    return only_place_list        
                   

def main():

    textfile = get_input()
    North, South = devide_North_South(textfile)
    
    cleaned_North = clean_line(North)
    cleaned_South = clean_line(South)

    only_places_North = only_place_name(cleaned_North)
    only_places_South = only_place_name(cleaned_South)
        
    write_to_North(only_places_North)
    write_to_South(only_places_South)
    
if __name__ == "__main__":
    main()
