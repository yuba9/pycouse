
while (1):
    x = int(input("enter a number: "))

    if (x % 7) == 0:
        print ("number divides by 7")
    else:
        print("number does not divide by 7")

print(x)

"""
Uri's comments:
==============

* This code works, but it runs in an endless loop. You should break when necessary.
  
"""
