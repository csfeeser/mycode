##WHAT READY PLAYER ONE AVATAR ARE YOU? - COURTNEY

##CREATING DICTIONARY
QUESTION1= {
            "question": "How would you spend time in the Oasis?",
            "A) Customizing one of a kind items": "AECH",
            "B) Trying to take down IOI": "ART3MIS",
            "C) Searching for Halliday's Easter eggs": "PARZIVAL",
            "D) Collecting Bounties on other Oasis users": "Ir0k"
            }


QUESTION2= {
            "question": "What are you most scared of?",
            "A) Scary Movies": "AECH",
            "B) Being imprisoned by IOI": "ART3MIS",
            "C) Losing friendship": "PARZIVAL",
            "D) Steampunk, Pirates and Tabbouleh": "Ir0k"
            }

QUESTION3= {
            "question": "In the Oasis, what rare item do you buy?",
            "A) Iron Giant": "AECH",
            "B) Clark Kent Glasses": "ART3MIS",
            "C) Holy Hand Grenade": "PARZIVAL",
            "D) Orb of Osuvox": "Ir0k"
            }

QUESTION4= {
            "question": "What set of personality traits fit you?",
            "A) Crafty, Intelligent": "AECH",
            "B) Smart, Passionate": "ART3MIS",
            "C) Loyal, Focused": "PARZIVAL",
            "D) Gullible, Scatterbrained": "Ir0k"
            }

QUESTION5= {
            "question": "Something your Avatar would most likely say or give as advice...",
            "A) She could actually be a 300 pound dude who lives in his momma's basement in suburban Detroit. And her name is Chuck": "AECH",
            "B) A real Gunter would risk everything to save the OASIS from IOI": "ART3MIS",
            "C) First to the key": "PARZIVAL",
            "D) To be honest, I have kind of a neck thing. It's like a carpel-tunnel deal, but with your neck": "Ir0k"
            }

##CREATING LISTS WITHIN DICTIONARY
QUESTION1_LIST= list(QUESTION1.keys())
QUESTION2_LIST= list(QUESTION2.keys())
QUESTION3_LIST= list(QUESTION3.keys())
QUESTION4_LIST= list(QUESTION4.keys())
QUESTION5_LIST= list(QUESTION5.keys())

##TIME FOR SLEEP COUNT
import time

##STARTING USER WELCOME INTERFACE
print('       ')
print("COMPLETE THIS QUIZ TO SEE WHICH") 
print("* READY PLAYER ONE AVATAR *") 
print("         YOU ARE?")
print('       ')
time.sleep(2)
print('       ')
print("   WELCOME TO THE OASIS!") 
print("MY NAME IS ANORAK THE CREATOR")
print('       ')
print("BEFORE YOU CAN ROAM AROUND") 
print("YOU NEED TO CHOOSE AN AVATAR!")
print('       ')
time.sleep(4.5)

##PLAY TO START
def playtostart():
    while True:
        ready = input("ARE YOU READY? CHOOSE Y TO CONTINUE: ").upper()
        if ready == "Y":
            print('       ')
            print("....READYING PLAYER ONE....")
            break
        else:
            print("CHOOSE Y TO CONTINUE")
            print('       ')
playtostart()
time.sleep(2)
print('       ')
print('       ')

##QUESTION1 BEGINS
print(QUESTION1["question"])
print(QUESTION1_LIST[1])
print(QUESTION1_LIST[2])
print(QUESTION1_LIST[3])
print(QUESTION1_LIST[4])

answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0} ##COUNTER

def Q1():
    #answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0} ##COUNTER
    global answer_counts
    while True:
        Q1ANSWER1 = input("PLAYER ONE>> ").upper()
        if Q1ANSWER1 in ["A", "B", "C", "D"]:##COUNTER
            answer_counts[Q1ANSWER1] += 1   ##COUNTER
            print("....LOADING NEXT QUESTION....")
            print('       ')
            print('       ')
            time.sleep(1.5)
            break
        else:
            print("404: COMPUTER SAYS NO")
Q1()


##QUESTION2 BEGINS
print(QUESTION2["question"])
print(QUESTION2_LIST[1])
print(QUESTION2_LIST[2])
print(QUESTION2_LIST[3])
print(QUESTION2_LIST[4])

def Q2():
    #answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0} ##COUNTER
    global answer_counts
    while True:
        Q2ANSWER2 = input("PLAYER ONE>> ").upper()
        if Q2ANSWER2 in ["A", "B", "C", "D"]:##COUNTER
            answer_counts[Q2ANSWER2] += 1    ##COUNTER
            print("....LOADING NEXT QUESTION....")
            print('       ')
            print('       ')
            time.sleep(1.5)
            break
        else:
            print("404: COMPUTER SAYS NO")
Q2()


##QUESTION3 BEGINS
print(QUESTION3["question"])
print(QUESTION3_LIST[1])
print(QUESTION3_LIST[2])
print(QUESTION3_LIST[3])
print(QUESTION3_LIST[4])

def Q3():
    #answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0} ##COUNTER
    global answer_counts
    while True:
        Q3ANSWER3 = input("PLAYER ONE>> ").upper()
        if Q3ANSWER3 in ["A", "B", "C", "D"]: ##COUNTER
            answer_counts[Q3ANSWER3] += 1 ##COUNTER
            print("....LOADING NEXT QUESTION....")
            print('       ')
            print('       ')
            time.sleep(1.5)
            break
        else:
            print("404: COMPUTER SAYS NO")
Q3()


##QUESTION4 BEGINS
print(QUESTION4["question"])
print(QUESTION4_LIST[1])
print(QUESTION4_LIST[2])
print(QUESTION4_LIST[3])
print(QUESTION4_LIST[4])

def Q4():
    #answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0}  ##COUNTER
    global answer_counts
    while True:
        Q4ANSWER4 = input("PLAYER ONE>> ").upper()
        if Q4ANSWER4 in ["A", "B", "C", "D"]:  ##COUNTER
            answer_counts[Q4ANSWER4] += 1  ##COUNTER
            print("....LOADING NEXT QUESTION....")
            print('       ')
            print('       ')
            time.sleep(1.5)
            break
        else:
            print("404: COMPUTER SAYS NO")
Q4()


##QUESTION5 BEGINS
print(QUESTION5["question"])
print(QUESTION5_LIST[1])
print(QUESTION5_LIST[2])
print(QUESTION5_LIST[3])
print(QUESTION5_LIST[4])

def Q5():
    #answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0} ##COUNTER
    global answer_counts
    while True:
        Q5ANSWER5 = input("PLAYER ONE>> ").upper()
        if Q5ANSWER5 in ["A", "B", "C", "D"]: ##COUNTER
            answer_counts[Q5ANSWER5] += 1 ##COUNTER
            print('       ')
            print('       ')
            time.sleep(1.0)
            break
        else:
            print("404: COMPUTER SAYS NO")
Q5()


##QUIZ COMPLETION
print('       ')
print("....CALCULATING PLAYER ONE RESULTS....")
#time.sleep(3)


####CALCULATING RESULT?????????????????????????????????
#answer_counts = ["A, B, C, D"]

AECH = answer_counts["A"]
ART3MIS = answer_counts["B"]
PARZIVAL = answer_counts["C"]
Ir0k = answer_counts["D"]

print(AECH, ART3MIS, PARZIVAL, Ir0k)

#for answer in answer_counts:
#    if answer == "A":
#        AECH += 1
#    elif answer == "B":
#        ART3MIS += 1
#    elif answer == "C":
#        PARZIVAL += 1
#    elif answer == "D":
#        Ir0k += 1

#if AECH == ART3MIS or AECH == PARZIVAL or AECH == Ir0k or ART3MIS == AECH or ART3MIS == PARZIVAL or ART3MIS == Ir0k or PARZIVAL == AECH or PARZIVAL == ART3MIS or PARZIVAL == Ir0k or Ir0k == AECH or Ir0k == ART3MIS or Ir0k == PARZIVAL:
#    print("...CONNECTION TERMINATED...")
if AECH > ART3MIS and AECH > PARZIVAL and AECH > Ir0k:
    print("YOUR AVATAR IS AECH")
    print("Welcome to my workshop...Touch Nothing")
elif ART3MIS > AECH and ART3MIS > PARZIVAL and ART3MIS > Ir0k:
    print("YOUR AVATAR IS ART3MIS")
    print("Ah, yes...Goddess of the Hunt")
elif PARZIVAL > AECH and PARZIVAL > ART3MIS and PARZIVAL > Ir0k:
    print("YOUR AVATAR IS PARZIVAL")
    print("People come to Oasis for all the things they can do but they stay because of the things they can be")
elif Ir0k > AECH and Ir0k > ART3MIS and Ir0k > PARZIVAL:
    print("YOUR AVATAR IS Ir0k")
    print("For Real...you need to go to Physical Therapy")
else:
    print("YOU'VE BEEN ZEROED OUT BY A KILLER CHUCKY")
    print("TRY AGAIN")
    print("...CONNECTION TERMINATED...")
