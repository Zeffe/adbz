import urllib, urllib2
import random

eSuffixes = [ "@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com",
              "@aol.com", "@msn.com", "@suddenlink.net", "@yahoo.co.uk" ]

word1 = ""
word2 = ""

def genUser():
    int1 = random.randint(0, 2335)
    int2 = random.randint(0, 2335)
    data = open("words.txt")
    
    for i, line in enumerate(data):
        if i == int1:
            word1 = line
        elif i == int2:
            word2 = line

    user = word1.capitalize() + word2.capitalize()

    if random.randint(0, 999)%3 is not 0:
        user += str(random.randint(0, 999))

    user = user.replace("\n", "")

    user += eSuffixes[random.randint(0, len(eSuffixes) - 1)]

    return user

