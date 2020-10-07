hardcoded_number=8
guess=int(input("Guess the number\n"))
if guess < hardcoded_number:
    print("guess is low")
elif guess > hardcoded_number:
    print("guess is high")
else:
    print("you gussed it") 