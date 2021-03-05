# Introduction_to_research_methods

In the amount_of_de.sh file you are going to come across this line:
WIKIPEDIA_PAGE=`wiki-cli -Pl nl Rijksuniversiteit Groningen`

This line loads the wikipediapage in a more usable variable
It uses wikipedia2text.
You have to download wikipedia2text for this shell script to be able to work (if you did not download it before).
You can do this by typing the following lines in your terminal:

git clone https://github.com/chrisbra/wikipedia2text 
sudo mv wikipedia2text/wikipedia2text /bin/wiki-cli
rm -Rf wikipedia2text

(after every line press enter)

wikipedia2text uses a text-browser, you have to download or already have one for it to be able to work.
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
# yum install links
[Fedora 22 & Later]
# dnf install links
[suse & openSUSE]
# zypper install links
[ArchLinux & Manjaro]
$ sudo pacman -S links
[Mageia]
# urpmi links

If you are on Ubuntu(linux) what I used as well use the sudo apt-get install links

To try and see of it works type in your terminal
links www.google.com

Something with the same text as google should show up.

If both wikipedia2text and (a working version of) a text-browser are installed, you can now download the file:
type the following line in your terminal to download the file:



