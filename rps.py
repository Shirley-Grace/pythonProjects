import random

options = ('rock', 'paper', 'scissors')
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('what do you choose(rock, paper , scissors)? ')

    print(f"player: {player}, computer: {computer}")

    if player == computer:
        print('Its a tie')
    elif player == 'rock' and computer == 'scissors':
        print('You win')
    elif  player == 'paper' and computer == 'rock':
        print('You win')
    elif  player == 'scissors' and computer == 'paper':
        print('You win')
    else:
        print('Computer wins')

    if not input("play again? (y/n)")== "y":
        playing = False

print("Thanks for playing!")

