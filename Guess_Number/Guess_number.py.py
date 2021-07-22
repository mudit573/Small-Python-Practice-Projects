import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number btw 1 and {x}:  3"))
        if guess < random_number:
            print("Sorry! guess again, Too low.")
        elif guess > random_number:
            print("Sorry! guess again ,Too high")


    print(f"Yay, Congrats. You have guessed the number {random_number} Correctly!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low!= high:
            guess = random.randint(low,high)
        else:
            guess =low # could be high b/c low=high

        feedback= input(f'is {guess} too high (H) , too Low (L), or Correct (C)  ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number,{guess},Coorrectly')



computer_guess(1000)
# guess(10)