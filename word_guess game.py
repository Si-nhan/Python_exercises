print("Start the game...")
word = "independence"
guesses = ''
turns = 5
while turns > 0: 
    failed = 0 
    for char in word: 
        if char in guesses: 
            print(char)
        else:
            print("_")
            failed += 1 
    if failed == 0: 
        print("You won")
        break 
    guess = input("Guess a character: ")
    guesses += guess 
    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print("You have", turns, "more guesses")
        if turns == 0: 
            print("You Lose")