import random

# library used to choose random word.
print('''Hi, Welcome to the game of Atlas.
        In this game, you will be given a country to guess
        If you guess it right, you win else you lose.''')
print("")
print("")
name = input("What is your name? ")
print("")
print("Best of Luck ! ", name)

countries = ['india', 'mexico', 'canada', 'brazil',
             'denmark', 'japan', 'china', 'ireland',
             'russia', 'poland', 'egypt', 'england']

countryname = random.choice(countries)
# this funcation will choose a random country

print("Guess the Country!!!")

guess = ''

no_of_turns = 12
# total no of turns

while no_of_turns > 0:

    wrong = 0
    # counts no of wrong attempts
    for i in countryname:

        # comparing entered character with the one  given in guess.
        if i in guess:
            print(i)

        else:
            print("_")

            # for every wrong attempt it will increase by 1.
            wrong += 1

    if wrong == 0:
        # if wrong is zero then it will print you win
        print("You Win !!!")

        # print country name
        print("The Country is: ", countryname)
        break

    # if user has entered wrong character it will ask the user to guess again
    inp = input("guess a character:")

    # every input character will be stored in guesses
    guess += inp

    # check input with the character in word
    if inp not in countryname:

        no_of_turns -= 1

        # if character doesnot match with the correct character it will print
        print("Wrong")

        # no of turns left
        print("You have", + no_of_turns, 'more guesses')

        if no_of_turns == 0:
            print("You Lose")