My system version and other things that need to be put down here:
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.2 LTS
Release:	20.04
Codename:	focal

My python function is 3.8.5

NLTK needs to be installed, the version that I am using is 3.5

Karora runs on :Ubuntu 16.04.7 LTS (GNU/Linux 4.15.0-99-generic x86_64)

How I got all the files for the Data directory
Go to the directory you want the file to be in using  cd
I logged in onto karora: ssh s3792412@karora.let.rug.nl 
(if you have a different rug number than mine, you should fill in that ofcourse)
type in your password
if the login is succesvol
I manually download every day of those 4 months, this will take you about 7 hours.
You can typ in the following line to get one day (in this case april the 30th)
zcat /net/corpora/twitter2/Tweets/2018/04/20180430:*.out.gz | /net/corpora/twitter2/tools/tweet2tab words user.location coordinates > ~/tweets_apr_30.txt

You have to do this for every day, here is another example
zcat /net/corpora/twitter2/Tweets/2018/03/20180309:*.out.gz | /net/corpora/twitter2/tools/tweet2tab words user.location coordinates > ~/tweets_mar_9.txt

And here is another one
zcat /net/corpora/twitter2/Tweets/2018/02/20180211:*.out.gz | /net/corpora/twitter2/tools/tweet2tab words user.location coordinates > ~/tweets_feb_11.txt

If you have downloaded every single one make sure that every file is in the directory the way it is in my github dipository

Git LFS needs to be installed
Link to how to install: https://packagecloud.io/github/git-lfs/install

I personally intstalled it in the way it says on this page
https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage

If you type in : git lfs install
and it says : git lfs initialized
Then you know that git lfs is installed correctly

What is the south of the Netherlands: the provinces of Zeeland, Limburg and North-Brabant.
What is the North of the Netherlands: the provinces of Drenthe, Friesland and Groningen.

Source for finding all places in the Netherlands: https://www.metatopos.eu/almanak.html

Bad words list source: https://gist.github.com/FrankHouweling/7fce4b89da4357744054
Good words list source: finding a good good words list was harder, the only thing I found was this https://www.theschoolofplay.nl/positief-verwoorden/#:~:text=Begrijpen%2C%20Begripsvol%2C%20Behulpzaam%2C%20Bejubelen,%2C%20Bloemrijk%2C%20Boeien%2C%20Briljant%2C so I copy pasted the words from the site and put them in a textfile. I put every word on a different line and deleted the capitals in between.

All zipcodes in the Netherlands have 4 numbers.

There are 2 python files.

The first one, cleaner.py, makes all_north_places.txt and all_south_places.txt from all_places_in_the_netherlands.txt
cleaner.py works with argv so you have to give the file as an argument, first make sure that all_places_in_the_netherlands.txt and cleaner.py are in the same directory and than typ in the following in the terminal: python3 cleaner.py all_places_in_the_netherlands.txt
Make sure to do this right the first time cause I am using append.

If you have all the files represented in the same directories as I have you can typ in: python3 worker.py
To get the results, you do have to be in FinalProject to make it work.

If you have any questions, here is my email address: huubexel@hotmail.com

Results:
The total amount of good tweets that were tweeted in the first 4 months of 2018 in the North of the netherlands is: 225378
The total amount of bad tweets that were tweeted in the first 4 months of 2018 in the North of the netherlands is: 264243
The total amount of good tweets that were tweeted in the first 4 months of 2018 in the South of the netherlands is: 566790
The total amount of bad tweets that were tweeted in the first 4 months of 2018 in the South of the netherlands is: 608427

