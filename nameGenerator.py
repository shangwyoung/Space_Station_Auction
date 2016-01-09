# What I have working for a name generator


 
import random

def lineCount(file):
    i=0
    with open(file, "r") as F:
        for i, l in enumerate(F):
            pass
        return i
# returns the number of lines-1 

def findWord(file):
    F= open(file, "r")
    length= lineCount(file)
    num= random.randint(0, length)
    for i, line in enumerate(F):
        if i==num:
            return line.strip()
#selects word from random line in file
        
def main():
     pref= findWord("prefixes.txt")
     place=findWord("places.txt")
     suff=findWord("suffixes.txt")
     # for testing I just made some .txt files of varying sizes 
     print(pref+" "+place+" "+suff)
# not of use; simple prints name for now in order to demonstrate functionality

main()
