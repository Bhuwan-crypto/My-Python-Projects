import random
number = random.randint(1,100)
guess = 0
while guess != number :
    guess = int (input("enter ur guess(1-100)"))
    if guess>number:
        print("too high")
    elif guess <number:
        print("too low!")
    else:
        print("correct")