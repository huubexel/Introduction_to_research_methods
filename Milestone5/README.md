# Introduction_to_research_methods

This readme is about the amount_of_de.sh shells script file, what it does (when all things that are below here are properly installed)
is it counts all occurrences of the article "de" in the Dutch Wikipedia page of the Rijksuniveristeit Groningen (link to wikipedia page):

(https://nl.wikipedia.org/wiki/Rijksuniversiteit_Groningen)

What part of the code does what, is commented in the code itself. Before running the code read this readme carefully.

The code can be found on this page:

https://raw.githubusercontent.com/hacxpiont/Introduction_to_research_methods/main/amount_of_de.sh/

It is stated down below how to download the code from your terminal.

The code gets the data for you and stores it very shortly for you, when it is finished with the data is removes the file automatically.

If you want to keep the stored file, remove the very last line of the code:

rm de_in_rug_nl.txt

the file de_in_rug_nl.txt should still be in the current working directory if you decide to remove the last line from the code.

In the amount_of_de.sh file you are going to come across this line:
WIKIPEDIA_PAGE=`wiki-cli -Pl nl Rijksuniversiteit Groningen`

This line loads the wikipediapage in a more usable variable
It uses wikipedia2text.
You have to download wikipedia2text for this shell script to be able to work (if you did not download it already).
You can do this by typing the following lines in your terminal:

git clone https://github.com/chrisbra/wikipedia2text 

sudo mv wikipedia2text/wikipedia2text /bin/wiki-cli

rm -Rf wikipedia2text

(after every line press enter)

wikipedia2text uses a text-browser, you have to download one or already have one for it to be able to work.
There are a few text-browser where it is certain that the program will work, these are the following:
- Links
- Links2
- ELinks
- Lynx
- w3m
- Netrik

I personally used Links.
You can download Links by using 1 of the following lines (depends on what kind of system you are using)

[Debian, Mint & Ubuntu]

$ sudo apt-get install links

[RHEL, CentOS & Fedora 21 & Older]

yum install links

[Fedora 22 & Later]

dnf install links

[suse & openSUSE]

zypper install links

[ArchLinux & Manjaro]

$ sudo pacman -S links

[Mageia]

urpmi links

If you are on Ubuntu(linux), thats what I used as well (distribution of linux I used = Ubuntu 20.04.2.0 LTS), use the sudo apt-get install links

To try and see if it works type in your terminal
links www.google.com

Something with the same text as google should show up. (afterwards you can just exit and restart the terminal again)

If both wikipedia2text and (a working version of) a text-browser are installed, you can now download the file:

Type the following line in your terminal to download the file:

wget https://raw.githubusercontent.com/hacxpiont/Introduction_to_research_methods/main/amount_of_de.sh

Or you could go to the github of hacxpiont and download it from there.

You now have the file.

Now you have to make it working, you can do this by typing this line once and pressing enter:

chmod ugo+x amount_of_de.sh

Everything is now set for it to be able to work:
Type this line in your terminal and press enter:

./amount_of_de.sh




