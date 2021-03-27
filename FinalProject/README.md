hier dus wat moois enzo


https://packagecloud.io/github/git-lfs/install
Ik moest dit downloaden om alle files te kunnen uploaden helaas.

Ik heb het geinstalleerd zoals het staat op deze pagina
https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage
en dan heb ik die download file in de programs file in home gezet.

Ik heb die gedownloade zipfile ge-extract in dat ding.

huub@huub-N552VX:~/Programs/Git_LFS/git-lfs-linux-amd64-v2.13.2$ 
Hier was ik nu

sudo ./install.sh           dit gedaan

als het goed is staat er dan iets van git lfs initialized ofso.

Toen geverifieerd dat de installatie succesvol is geweest met het proberen van deze code:
git lfs install
en als het goed is staat er dan nog een keer 
git lfs initialized.

What is the south of the Netherlands: the provinces of Zeeland, Limburg and North-Brabant.
What is the North of the Netherlands: the provinces of Drenthe, Friesland and Groningen.

What Do I need besides the data that I already uploaded, A list of places in these provinces and a list of happy and negative words. Than I have to make a python code that searches out the tweets that are happy and those that are sad. And last but not least write a report about this.

This is where i found the list: https://www.metatopos.eu/almanak.html

I now have a list with the places of the north of the netherlands and a list with the places of the south of the Netherlands.

Now I need a good words and bad words list.

Bad words list: https://gist.github.com/FrankHouweling/7fce4b89da4357744054
Good words list: finding a good good words list was harder, the only thing I found was this https://www.theschoolofplay.nl/positief-verwoorden/#:~:text=Begrijpen%2C%20Begripsvol%2C%20Behulpzaam%2C%20Bejubelen,%2C%20Bloemrijk%2C%20Boeien%2C%20Briljant%2C so I copy pasted the words from the site and put them in a textfile. I put every word on a different line and deleted the capitals in between.

All zipcodes in the Netherlands have 4 numbers.

Wat mogelijk een goed idee is voor de toekomst, voor het verdere onderzoek is om te kijken naar de provincies invidueel dan alleen maar het verschil tussen noord en zuid, je zou dan in principe elke provincie apart kunnen doen wat nog wat accurater is dan alleen het verschil tussen noord en zuid.

De plaatslijst voor zowel noord als zuid is nu ook klaar, dus nu moet ik die grote python code maken die uitzoekt of een tweet blij of niet blij is. Daarnaast moet ik dan kijken waar dat weg kan komen, ik ga eerst de plek gebruiken en dan hoop ik dat dat genoeg is.

Ik denk dat het ook wel cool is dat je op het eind kunt laten zien hoeveel  procent blij is van de tweets en hoeveel procent van de tweets boos is of iets in die richting.

How Netherlands as a language works is if something is possitive that immediatly rules out the negative except if you place one of those 4 "niet" words in front of it.

Bad words lijst aangepast.

Nu moet je dus eerst de tweets hebben uit het noorden en het zuiden, nou dat is prima hoe ik zie dat het werkt is als volgt je hebt de tweet dan heb je en tab en daarna heb je dus die plek als die er mogelijk is, als er niks achter staat dan is dat jammer maar ja helaas. Wat ook kan zijn dat daar coordinaten staan maar daar ga ik niks mee doen dus eigenlijk wat er moet gebeuren is het volgende.

Tekst staat hier \t (tab) plaats

Dan moet je kijken is er een deel (of de complete naam) van die plaats die match met een plaatst in de set. (dit is het lastigste).
Is dit waar dan neem je index 0 en 1 van die zin.
Daarna ga je kijken of er een vrolijk of niet vrolijk woord instaat
Dan ga je met die regels die je bedacht hebt ga je kijken bij welke van de 2 die hoort of dat ie bij geen van 2 behoort,
weet je dan weer die bij hoort dan tel je dat bij die counter op.


https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/


# het enig wat je kunt doen is kijken of er een deel van dat woord in het totaal zit van index [1]
# dus wat je dan ook moet doen is elke mogelijkheid daarvoor kijken of die in 1 van die 2 bestanden met plaatsen zit 
# en is dat het geval dan moet diezelfde tweet ook gekeken worden of die positief of negatief is en is dat het geval 
# dan krijgt of noord of zuid er 1 punt bij voor of vrolijk of niet vrolijk.
