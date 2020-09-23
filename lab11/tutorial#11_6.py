from random import randint

x = randint(1, 100)

while True:
    try:
        y = int(input("Please guess number: "))
        if x == y:
            print("it's a match")
            break
        if x > y:
            print("the number you guessed is too small")
        else:
            print("the number you guessed is too big")
    except ValueError:
        print("The input have to be a number")

"""
Uri's comments:
==============

* Very good! This code works.
  
"""
