# the goal is to count the amount of chosen integers associated with the user's choices,
# and then tally up the results for a specific output at the end (a=1=Ravenclaw : b=2=Hufflepuff
# c=3=Gryffindor : d=4=Slytherin)
# Whichever amount of integers associated with the user's responses is greatest 
# will determine their house.

#!/usr/bin/env python3
## made this a python shebang, not a bash shebang


## in a dictionary, there must always be both a key and a value
## since the first answer is always ravenclaw, second hufflepuff, etc
## I put those answers in a list. That list is now the value
## of the key "answers"

question1= {"question": "Choose one of the four classical elements",
            "answers": ["water",
                        "air",
                        "fire",
                        "earth"]
           }

question2= {"question": "Choose your favorite color out of the ones listed below:",
            "answers": ["blue",
                        "yellow",
                        "red",
                        "green"]
           }

question3= {"question": "Choose the word that best describes you:",
            "answers": ["creative",
                        "kind",
                        "courageous",
                        "ambitious"]
           }

question4= {"question": "what would be your favorite class at hogwarts:",
            "answers": ["history of magic",
                        "herbology",
                        "defense against the dark arts",
                        "potions"]
            }

question5= {"question": "you would be most hurt if someone called you?:",
            "answers": ["dumb",
                        "mean",
                        "dull",
                        "weak"]
           }
