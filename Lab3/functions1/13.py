print('Hello! What is your name?')
name=input()
a,b=1,20
import random
number=random.randint(a,b)
print(f'Well, {name}, I am thinking of a number between {a} and {b}')
print('Take a guess.')
def guessing():
    g=1
    while True:
        guess=int(input())
        if guess==number:
            return g
        elif guess<number:
            print("Your guess is too low.")
            print("Take a guess.")
        elif guess>number:
            print("Your guess is too much.")
            print("Take a guess.")
        g+=1
g=(guessing())    
print(f'Good job, {name}! You guessed my number in {g} guesses!')


