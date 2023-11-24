import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Guess a random number between 1 and {x}: ")) 
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")
    
    print(f"Grat: {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or Correct").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"correct {guess}")

computer_guess(10)

guess(10)