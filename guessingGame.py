import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("Type a number between 1-9: "))
    if (introString > number):
        print("Your number is large. Try something smaller.")
    elif (introString == number):
        print("Congratulation! You guessed it correct :)")
    else :
        print("Your number guess is less. Try something larger")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("Oh! You are out of chances :( ")
