import random
number = random.randint(1, 15 )
trials = 1
name =input("Hello, What is your name?")
print("Hello", name + ".")
question = input("Would you like to play a game?[Y/N]")
if question ==  "n":
    print("Oh..Okay")
if question == "y":
    print("I am thinking of a number between 1 t 10.What is it?")
    guess  = int(input("Have a guess: "))
    if guess > number:
        print ("Guess Lower")
    if guess < number:
        print("Guess Higher")
    while guess != number:
        trials +=1
        guess = int(input("Try Again: "))
        if guess < number :
            print("Guess Higher")
    if guess == number :
        print("You are correct!the number is", number, \
              "and it only took", trials, "trials!")


