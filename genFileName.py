from random import shuffle
from random import randint 
import os,sys


if not os.path.isdir("./word_files"):
    print("word file directory not found")
    sys.exit()
        

def randomFileName():
    adjvs = []
    advbs = []
    anims = []
    nouns = []
    verbs = []

    with open("./word_files/adjectives.txt","r") as f:
        adjvs = f.readlines()
    f.close()

    with open("./word_files/adverbs.txt","r") as f:
        advbs = f.readlines()
    f.close()

    with open("./word_files/animals.txt","r") as f:
        anims = f.readlines()
    f.close()

    with open("./word_files/nouns.txt","r") as f:
        nouns = f.readlines()
    f.close()

    with open("./word_files/verbs.txt","r") as f:
        verbs = f.readlines()
    f.close()

    shuffle(adjvs)
    shuffle(advbs)
    shuffle(anims)
    shuffle(nouns)
    shuffle(verbs)

    #WobblyEdibleComputers
    #print s[0].upper()


    if randint(0,9999) % 2 == 0:
        one = verbs[0][0].upper() + verbs[0][1:].lower()
        shuffle(verbs)
    else:
        one = advbs[0][0].upper() + advbs[0][1:].lower()

    if randint(0,9999) % 2 == 0:
        two = verbs[0][0].upper() + verbs[0][1:].lower()
    else:
        two = adjvs[0][0].upper() + adjvs[0][1:].lower()

    if randint(0,9999) % 2 == 0:
        thr = nouns[0][0].upper() + nouns[0][1:].lower()
    else:
        thr = anims[0][0].upper() + anims[0][1:].lower()

    word = one.strip()+two.strip()+thr.strip()
    
    return word

if __name__=='__main__':
    print(randomFileName())






