import random

def guess(x):

    random_num = random.randint(1,x)
    guess = 0
    while random_num != guess:
        guess=int(input(f"Guess a number between 1 and {x} :"))
        if(guess>random_num):
            print("The number is too high! guess another.... ")
        elif(guess<random_num):
            print("The numbert is too low! guess another.... ")
    print("You guessed it right.... congrats")
x = int(input("Enter the limit : "))
guess(x)
