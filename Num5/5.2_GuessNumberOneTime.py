import random
rand_number=random.randint(1,100)
guess_number=eval(input("enter your number\n"))
while guess_number != rand_number:
    if guess_number>rand_number:
        print("too high\n")
    elif guess_number<rand_number:
        print("too low\n")

print("you win")