# Design a word jumble game
# L P E P S A
# -> [1] ? 
# -> [Hint] This is a fruit
# -> [2] APPLES

import random

# Collection of words
L = ["apples", "laptop", "mangoes", "computer", "mobile", "hyundai", "mercedes", "samsung"]
random.shuffle(L)

# -------------------------------------- Start of task

points = 0

# Repeat until all words are done
# Pick a word
for word in L:

    # Jumble the word
    temp = list(word)
    random.shuffle(temp)
    jword = ''.join(temp)
    

    # Show the word to the user
    print("-> ", jword)

    # Ask for the user input
    uword = input("Can you guess? ")

    # Compare the user input with original word
    # Update points
    if(uword == word):
        print("Correct")
        points += 1
    else:
        print("Incorrect")
    
# -------------------------------------- End of task

# Print the results
if(points > 6):
    print("Excellent Playing!")
elif(3 <= points <= 6):
    print("Good")
else:
    print("Improvement needed")
