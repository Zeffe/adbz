import urllib, urllib2
import random
import os, time
import thread

eSuffixes = [ "@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com",
              "@aol.com", "@msn.com", "@suddenlink.net", "@yahoo.co.uk" ]

proxies = []

word1 = ""
word2 = ""

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print "\n Main Menu\n\n\tCoded by Zeffer and 133spider\n\n Available Commands:\n\n\tinit\t\tInitialize program\n\tgen\t\tGenerates unique emails to an output file.\n\tinfo\t\tREADME\n\texit\t\texit program\n"
    interpret(raw_input(" [>] Please enter a command to use: "))

def genUser():
    int1 = random.randint(0, 2335)
    int2 = random.randint(0, 2335)
    data = open("words.txt")

    word1 = ""
    word2 = ""
    
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

def vote(user, trope):                                      #1685 WC
    data = { "method":"dxp_vote", "email":user, "store_id":"1542", "opt_in":"no" }
    data = urllib.urlencode(data)

    get = urllib2.urlopen("http://api.dominosdxp.com/api_voting.php", data)
    #handleData = get.Read()
    get.close()

    print " [+] Successfully voted with " + user

def interpret(command):
    if command == "exit":
        exit()
    elif command == "init":
        x = raw_input("Are you sure you want to vote 100 times without proxies? [Y/N]: ")
        while True:
            if x.lower() == "y":
                for i in range(100):
                    thread.start_new_thread(vote,(genUser(), "trope"))
                    time.sleep(int(150)/float(1000))
                print ""
                print "Successfully voted with 100 users."
            elif x.lower() == "n":
                break
    elif command == "info":
        print ""
        print " @Generates thousands upon thousands of unique emails."
        print ""
        print " @Uses a different proxy on each connection."
        print ""
        print " @Reuses usernames daily to ensure no suspicions are raised."
        print ""
        print " @Limits itself in time to ensure no suspicions are raised."
        print ""
        raw_input()
        menu()
    elif command == "gen":
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            gen = raw_input(" [>] How many emails would you like to generate?: ")
            try:
                if (int(gen) > 0):
                    genAmnt = int(gen)
                    break
            except:
                print " @Error | Number must be numeric and larger than 0."
        while True:
            out = raw_input(" [>] What path would you like the emails to be written to?: ")
            if out is not "":
                break

        _file = open(out + ".txt", "w")

        print ""
        
        for i in range(genAmnt):
            _user = genUser()
            _file.write(_user + "\n")
            print " [+] " + _user

        _file.close()
        
        print ""
        raw_input("Finished!")
        menu()
    else:
        menu()

menu()
