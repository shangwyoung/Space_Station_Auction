# CardGenerator.py

# janky as hell and uncommented; for meeting reference (I'll suss out comments and logic as of tonight/tomorrow morning)
# so far, handles card name and stats, but does so as a list of lists (cards)

import random
import card


def makeList(file):
    F= open(file, "r")
    words=[]
    for line in F:
        line= line.strip()
        words.append(line)
    return words

def makeName(prefList, placeList, suffList):
    maximum= len(prefList)
    index=random.randint(0,maximum)
    prefWord= prefList[index]
    
    maximum= len(placeList)
    index=random.randint(0,maximum)
    placeWord= placeList[index]
 
    maximum= len(suffList)
    index=random.randint(0,maximum)
    suffWord= suffList[index]
    
    Name= concat(prefWord, placeWord, suffWord)
    
    return Name
    

def concat(pref, place, suff):
    name= pref+" "+place+" "+suff
    return name

def makingDeck(deck)
    prefixList=makeList("prefixes.txt")
    placeList=makeList("places.txt")
    suffixList=makeList("suffixes.txt")
    

    cards=[]
    for i in len(deck):
        individualCard=[]
        name=makeName(prefixList, placeList, suffixList)
        individualCard.append(name)
        scienceValue= random.randint(0,10)
        individualCard.append(scienceValue)
        ecologyValue= random.randint (0,10)
        individualCard.append(ecologyValue)
        cultureValue= random.randint(0,10)
        individualCard.append(cultureValue)
        commerceValue= random.randint(0,10)
        individualCard.append(commerceValue)
        industryValue= random.randint(0,10)
        individualCard.append(industryValue)
        cards.append(individualCard)


