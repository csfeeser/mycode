# Lists and Dictionaries with Dell Codes

### Lab Objective

**The objective of this lab is to learn to send HTTP GETs to the Redfish OOB API, common to most servers.** To learn more about RedFish, we will be deploying the RedFish Mock-up Server. This server was created to help with the creation of the RedFish standards. Before you start, visit and review the following repository.

### Introduction to Lists and Dictionaries

Let's start by taking a look at a Python list! Depending on your background, you might recognize this as an array in a language like JSON. **A list is an ordered sequence of element.** Every element in a list has an index number to indicate its position, so finding information in a list is by using the appropriate number. Observe below:

```python
#         Index counts ALWAYS start at zero!
#             ↓0           ↓1           ↓2
pokedex= ["bulbasaur", "squirtle", "charmander"]
```

In the above example, `bulbasaur` is element `0`. `charmander` is element `2`. Don't forget to always start counting from zero! Lists are an *extremely* common data type in almost every language.

Now let's have a look at a Python dictionary. **A dictionary is an unordered collection of key/value pairs.** Unlike lists, dictionaries do not have an index, so you can put the contents of a dictionary in any order that you like. That is because dictionaries find information by its key. Observe below:

```python
#              ↓KEY         ↓VALUE
poke_dict= {"charmander": "fire type"
              "squirtle": "water type",
             "bulbasaur": "grass type",
           }
```

Notice that the order of the Pokemon has changed. This **does not matter!** If we want to know a Pokemon's type, we only have to ask the dictionary what is the value of the matching key. The key `squirtle` will always return `water type` no matter what order we put our dictionary in. Dictionaries are complex, but are also an *extremely* common and effective data type!

### Procedure

1. Let's write a Python script that enables a user to do the following:
     - input the name of a server (R450, XR11, etc.)
     - breaks down each part of the server's code name, telling us the following:
        - chassis type
        - number of sockets
        - generation number
        - processor type

0. We're going to want to include some data in our Python script to represent socket count and generation number. Remember lists always start counting from 0.

    ```python
    # This is a list
    socket_list = [            # Index:
             "NA",             # 0
             "1 Socket",       # 1
             "1 Socket",       # 2
             "1 Socket",       # 3
             "2 Sockets",      # 4
             "2 Sockets",      # 5
             "2 Sockets",      # 6
             "2 Sockets",      # 7
             "2 or 4 sockets", # 8
             "4 Sockets"       # 9
            ]

    # This is a list
    gen_list = [
             "Gen 10",
             "Gen 11",
             "Gen 12",
             "Gen 13",
             "Gen 14",
             "Gen 15",
             "Gen 16",
             "Gen 17",
             "Gen 18",
             "Gen 19"
            ]
    ```

    <details>
    <summary>What is element 2 from gen_list? <i>(gen_list[2])</i></summary>
    <br>
    "Gen 12"

    Index position 2 is the third index number... 0, 1, 2!
    </details>

0. We're also going to want data on chassis type and processor. We'll represent that information inside two dictionaries.

    ```python
    chassis_dict = {
              "C": "Compute optimized hyper-scale server",
              "F": "Rack-based sleds for FX2/FX2s enclosure",
              "M": "Modular Blade server",
             "MX": "Modular Blade server",
              "R": "Rack-mountable",
             "XE": "Extreme performance and storage",
             "XR": "Extreme ruggedness"
            }

    proc_dict = {
             "0": "Intel",
             "5": "AMD"
            }        
    ```

    <details>
    <summary>What key would return "Modular Blade Server?"</i></summary>
    <br>
    "M" OR "MX"!

    Note that two keys can have the same value in a dictionary. However, all keys MUST be unique.
    </details>

0. Now that we have our data we can start building Python code around it. The full version of this code can be found at the end of the lab (you may want to skip ahead and execute it first, then come back). Let's break down how this code works, chunk by chunk. The code below does the following:
  - `os.system('clear')` tells Linux to "clear" the screen, giving us a fresh viewing area. Nice!
  - `input()` is a Python *function* that allows a user to answer a question prompt and save their answer inside a variable.
  - `re.compile()` is a function imported from the `re` (RegEx) module. Modules are libraries of additional tools Python can import and use.
     - Not a RegEx master? [Click here](https://regex101.com/r/iApAKR/1) and see how a Dell server name like "R450" could be picked apart into four different pieces.
  - `if match` will confirm if our regular expression was able to confirm a match to the user's input. If so, each piece of the input will be saved into four variables (`code1`, `code2`, etc.)  

    ```python
    import re
    import os

    os.system('clear')
    code = input("Enter a server code: ")

        # PARSING THE USER INPUT START #################################################
        # This REGEX code snippet is *very* common for parsing input. Use it often!
        # This pattern is looking for letters only, followed by three digits
        # c1 will capture letters, and; c2, c3, and c4 will each collect a single digit
        # code = "R450" would be an example of a MATCH
        # code = "wxq3" would NOT match
        # Could we write a better pattern, YOU BET! Go for it.
        pattern = re.compile(r"""
                                 (?P<c1>[a-zA_Z]+)
                                 (?P<c2>\d)
                                 (?P<c3>\d)
                                 (?P<c4>\d)
                              """, re.VERBOSE)
        match = pattern.match(code)
        if match:
            # If we get this far, the input matched the REGEX
            code1 = match.group("c1").upper()
            code2 = int(match.group("c2"))
            code3 = int(match.group("c3"))
            code4 = match.group("c4")
    ```

0. In programming, you should never assume that a user will type in perfectly correct input. So we'll add a section of code that ONLY activates if the user types in something wrong.
   - `for loops` are used to iterate over (go piece by piece over) data. To show our wayward user what are actually valid characters in a Dell server name, these for loops return each piece of a list or dictionary which is then `print()`ed to the screen!
   -  `+=` will force a variable to increase its value by adding to itself.
   - `exit()` is a function that will force the program to end prematurely.

    ```python
    else:
       # If this runs, the user entered an invalid code, so output help info.
       # FIRST ERROR HANDLING OUTPUT STARTS HERE
       print(f"The first character is the chassis type")
       print(f"---------------------------------------------")
       for key in chassis_dict:
           print (f"{key} = {chassis_dict[key]}")

       print(f"\nThe second character is the socket count")
       print(f"---------------------------------------------")
       # Use the index value (0-9) to reference each item in a list
       i=0
       for item in socket_list:
           print (f"{i} = {item}")
           i +=1

       print(f"\nThe third character is the generation")
       print(f"---------------------------------------------")
       # Use the idex value (0-9) to reference each item in a list
       i=0
       for item in gen_list:
           print (f"{i} = {item}")
           i +=1

       print(f"\nThe fourth character is the CPU type")
       print(f"---------------------------------------------")
       # Use the ".keys" method to lookup the key of each dictionary item
       for key in proc_dict:
           print (f"{key} = {proc_dict[key]}")
       print(f"---------------------------------------------\n")
       print(f" You entered \"{code}\" which is NOT a dell server code\n")
       print(" You must enter a valid code like r450 or mx345\n")
       print(" Reference the above and PLEASE TRY AGAIN\n")
       # NOTE THE NEXT LINE = EXIT!       
       exit() # No use continuing. Exit the script.
       # FIRST ERROR HANDLING ENDS HERE
    ```

0. At this point in the script if we didn't already `exit()` out of the code, our regular expression must have found a match! We are now ready to break down what each part of the Dell server name means! The next piece of our script will do the following:
  - test if each letter or number in the server code is actually inside the appropriate list or dictionary.
  - if it IS present, we will print what that letter or number means (chassis type, socket count, etc.)    
  - if it is NOT present, we will inform the user of what a valid option would have been.

    ```python
    # If we got this far, all four codes passed the regex test,
    # but additional validity testing is necessary
    print(f"Looking up Dell {code1}{code2}{code3}{code4}:")

    if code1 in chassis_dict:
        # If code1 can be found in the code1 dictionary, it is valid, so print it.
        print(f"  {code1} = {chassis_dict[code1]}")
    else:
        # Else the code was not found so start error handling
        # code1 ERROR HANDLING STARTS
        print(f" {code1} is invalid, valid codes are:")
        for key in chassis_dict:
            print (f"    {key} = {chassis_dict[key]}")
        #code1 ERROR HANDLING ENDS

    if 1 <= code2 <= 9:
        # If code2 is a single digit 1-9, it is valid, print it
        print(f"  {code2} = {socket_list[code2]}")
    else:
        # Else it is not valid, so handle the error
        #code2 ERROR HANDLING STARTS
        print(f"  {code2} is invalid. Valid CPU socket codes are:")
        i=0
        for item in socket_list:
            print (f"    {i} = {item}")
            i +=1
        #code2 ERROR HANDLING ENDS    

    if 0 <= code3 <= 9:
       # If code3 is a single digit 0-9, it is valid, print it
       print(f"  {code3} = {gen_list[code3]}")
    else:
        # Hmmm, this should NEVER happen, but let's write a defensive
        # error handler in spite of that.
        #code3 ERROR HANDLING STARTS
        print(f" error: {code3} Must be 0 to 9")
        i=0
        for item in gen_list:
            print (f" {i} = {item}")
            i +=1
        #code3 ERROR HANDLING ENDS

    if code4 in proc_dict:
        # If code4 is found, print it
        # Wow, error handling with dictionaries seems easier!
        print(f"  {code4} = {proc_dict[code4]}")
    else:
        # else the code was not found, so handle the error
        #code4 ERROR HANDLING STARTS
        print(f"  {code4} is invalid, here are valid options:")
        for key in proc_dict:
           print (f"     {key} = {proc_dict[key]}")
        #code4 ERROR HANDLING ENDS
    ```

0. Now let's put all of this together! Create a file named `dell_code_reader.py`.

    `student@bchd:~$` `vim ~/mycode/dell_code_reader.py`

    ```Python
    #!/usr/bin/env python3

    # Import libraries that will be used in this script
    import re
    import os

    def main():

        # This is a dictionary:
        chassis_dict = {
                  "C": "Compute optimized hyper-scale server",
                  "F": "Rack-based sleds for FX2/FX2s enclosure",
                  "M": "Modular Blade server",
                 "MX": "Modular Blade server",
                  "R": "Rack-mountable",
                 "XE": "Extreme performance and storage",
                 "XR": "Extreme ruggedness"
                }

        # This is a list:
        socket_list = [
                 "NA",
                 "1 Socket",
                 "1 Socket",
                 "1 Socket",
                 "2 Sockets",
                 "2 Sockets",
                 "2 Sockets",
                 "2 Sockets",
                 "2 or 4 sockets",
                 "4 Sockets"
                ]

        # This is a list
        gen_list = [
                 "Gen 10",
                 "Gen 11",
                 "Gen 12",
                 "Gen 13",
                 "Gen 14",
                 "Gen 15",
                 "Gen 16",
                 "Gen 17",
                 "Gen 18",
                 "Gen 19"
                ]

        # This is a dictionary
        proc_dict = {
                "0": "Intel",
                "5": "AMD"
                }

        os.system('clear')
        code = input("Enter a server code: ")

        # PARSING THE USER INPUT START #################################################
        # This REGEX code snippet is *very* common for parsing input. Use it often!
        # This pattern is looking for letters only, followed by three digits
        # c1 will capture letters, and; c2, c3, and c4 will each collect a single digit
        # code = "R450" would be an example of a MATCH
        # code = "wxq3" would NOT match
        # Could we write a better pattern, YOU BET! Go for it.
        pattern = re.compile(r"""
                                 (?P<c1>[a-zA_Z]+)
                                 (?P<c2>\d)
                                 (?P<c3>\d)
                                 (?P<c4>\d)
                              """, re.VERBOSE)
        match = pattern.match(code)
        if match:
            # If we get this far, the input matched the REGEX
            code1 = match.group("c1").upper()
            code2 = int(match.group("c2"))
            code3 = int(match.group("c3"))
            code4 = match.group("c4")
        # PARSING THE USER INPUT END #####################################################
        else:
           # If this runs, the user entered an invalid code, so output help info.
           # FIRST ERROR HANDLING OUTPUT STARTS HERE
           print(f"The first character is the chassis type")
           print(f"---------------------------------------------")
           # Use the ".keys" method to lookup the key of each dictionary item
           for key in chassis_dict:
               print (f"{key} = {chassis_dict[key]}")

           print(f"\nThe second character is the socket count")
           print(f"---------------------------------------------")
           # Use the idex value (0-9) to reference each item in a list
           i=0
           for item in socket_list:
               print (f"{i} = {item}")
               i +=1

           print(f"\nThe third character is the generation")
           print(f"---------------------------------------------")
           # Use the idex value (0-9) to reference each item in a list
           i=0
           for item in gen_list:
               print (f"{i} = {item}")
               i +=1

           print(f"\nThe fourth character is the CPU type")
           print(f"---------------------------------------------")
           # Use the ".keys" method to lookup the key of each dictionary item
           for key in proc_dict:
               print (f"{key} = {proc_dict[key]}")
           print(f"---------------------------------------------\n")
           print(f" You entered \"{code}\" which is NOT a dell server code\n")
           print(" You must enter a valid code like r450 or mx345\n")
           print(" Reference the above and PLEASE TRY AGAIN\n")
           # NOTE THE NEXT LINE = EXIT!       
           exit() # No use continuing. Exit the script.
           # FIRST ERROR HANDLING ENDS HERE

        # If we got this far, all four codes passed the regex test,
        # but additional validity testing is necessary
        print(f"Looking up Dell {code1}{code2}{code3}{code4}:")

        if code1 in chassis_dict:
            # If code1 can be found in the code1 dictionary, it is valid, so print it.
            print(f"  {code1} = {chassis_dict[code1]}")
        else:
            # Else the code was not found so start error handling
            # code1 ERROR HANDLING STARTS
            print(f" {code1} is invalid, valid codes are:")
            for key in chassis_dict:
                print (f"    {key} = {chassis_dict[key]}")
            #code1 ERROR HANDLING ENDS

        if 1 <= code2 <= 9:
            # If code2 is a single digit 1-9, it is valid, print it
            print(f"  {code2} = {socket_list[code2]}")
        else:
            # Else it is not valid, so handle the error
            #code2 ERROR HANDLING STARTS
            print(f"  {code2} is invalid. Valid CPU socket codes are:")
            i=0
            for item in socket_list:
                print (f"    {i} = {item}")
                i +=1
            #code2 ERROR HANDLING ENDS    

        if 0 <= code3 <= 9:
           # If code3 is a single digit 0-9, it is valid, print it
           print(f"  {code3} = {gen_list[code3]}")
        else:
            # Hmmm, this should NEVER happen, but let's write a defensive
            # error handler in spite of that.
            #code3 ERROR HANDLING STARTS
            print(f" error: {code3} Must be 0 to 9")
            i=0
            for item in gen_list:
                print (f" {i} = {item}")
                i +=1
            #code3 ERROR HANDLING ENDS

        if code4 in proc_dict:
            # If code4 is found, print it
            # Wow, error handling with dictionaries seems easier!
            print(f"  {code4} = {proc_dict[code4]}")
        else:
            # else the code was not found, so handle the error
            #code4 ERROR HANDLING STARTS
            print(f"  {code4} is invalid, here are valid options:")
            for key in proc_dict:
               print (f"     {key} = {proc_dict[key]}")
            #code4 ERROR HANDLING ENDS

    if __name__ == "__main__":
        main()           
    ```

0. Now let's execute the script. When prompted, try out a few legit Dell server code names like `r450` or `xr11`. Then try some codes that do not exist, like `asdf1234` or `z001`!

    `student@bchd:~$` `python3 ~/mycode/dell_code_reader.py`

0. **IN CONCLUSION:** This code was developed entirely around the data structure of the lists and dictionaries we wrote. Properly organized data is easy to read and easy to program with. If your data is poorly organized, you will have poor code. "Garbage in, garbage out," as they say. It is *critical* to understand how lists and dictionaries work moving forward, so don't be shy and ask your instructor for help if you need further explanation and/or examples!

0. **CUSTOMIZATION:** Suppose the folks from Dell decided they would take a cue from Star Trek and develop a new server chassis made from the same metal as the starship U.S.S. Enterprise! Adjust your code so the chassis `Tritanium`, represented by the letter `T`, is a valid chassis type.

    <details>
    <summary>Click here for the solution!</summary>
    <br>

    ```python3
    chassis_dict = {
              "T": "Tritanium mined from the planet Argus X"   # NEW LINE
              "C": "Compute optimized hyper-scale server",
              "F": "Rack-based sleds for FX2/FX2s enclosure",
              "M": "Modular Blade server",
             "MX": "Modular Blade server",
              "R": "Rack-mountable",
             "XE": "Extreme performance and storage",
             "XR": "Extreme ruggedness"
            }
    ```

    </details>
0. That's it for this lab. If you are tracking your work on an SCM, perform the following operations.

    - `cd ~/mycode`
    - `git status`
    - `git add /home/student/mycode/*`
    - `git commit -m "lists and dictionaries with python"`
    - `git push origin`
    - `cd ~/`

<br><br><div align="center">

![Alta3 Logo](https://labs.alta3.com/images/Alta3-logo_large.png)

</div>
