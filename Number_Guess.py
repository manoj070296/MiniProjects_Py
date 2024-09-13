import random
print("Welcome to number guesser")

user_input=input("Enter a number: ")
if user_input.isdigit():
    user_input=int(user_input)
    if user_input<0:
        print("Please type a number greater than  zero")
else:
    print("Please enter a digit next time !!")
rd=random.randint(0,user_input)
guesses=0
while True:
    guesses += 1
    Guess = input("Guess a number: ")
    if Guess.isdigit():
        Guess = int(Guess)
    else:
        print("enter a number next time")
        continue
    if Guess==user_input:
            print("You got it!!!")
            break
    else:
            print("Better luck next time")
print("You did this in",guesses,"guesses")
