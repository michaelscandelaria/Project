# 75-BALL BINGO BONANZA!

#### Video Demo:  https://youtu.be/5_IrLN85Ges

#### Description:
In this project, I constructed a custom bingo game on Python based on the most common format of
the game in the United States, the 75-ball bingo game. In this game, each player has a 5x5 grid
of numbers in a card, meaning there are 5 rows and 5 columns containing numbers in each card. Thus, there
are 24 randomly-selected numbers in each card since the center position (C3) is a free spot. These
numbers should be positive integers within the range of 1-75 inclusive, meaning that the numbers 1
and 75 can also be selected as possible number values on the card.

The first step for the player is obtaining their unique bingo card. The player can either generate one
at random or customize their own card. If the player wants to customize their own card, they have to
follow a set of specific rules, which the randomly-generated card also follows. The **initializer**
function ensures that the player's card fulfills all of these rules.

1. All numbers in the first column (leftmost) should be numbers from 1-15 inclusive.
2. All numbers in the second column should be numbers from 16-30 inclusive.
3. All numbers in the third column (except for C3) should be numbers from 31-45 inclusive.
4. All numbers in the fourth column should be numbers from 46-60 inclusive.
5. All numbers in the fifth column (rightmost) should be numbers from 61-75 inclusive.
6. There cannot be any repeating numbers in the card.

Before the game starts, the program automatically marks the C3 spot since this is considered
a free spot. So, all players start the game with one mark in their card already.

After the player chooses a card, they can play the game in either normal mode or jackpot mode.
In normal mode, they have to mark all the numbers within any row, column, or diagonal in their
card before calling bingo. Take note that the diagonal has to pass through the C3 position for
it to be valid. In jackpot mode, on the other hand, the player has to mark all the numbers in their
entire card before calling bingo. The player can only mark a specific number in their card if
that specific number has been drawn already in either the current round or in any previous round.

Once the player starts the game, the gamemaster will start drawing a number from 1-75 inclusive
at random for each round. Again, there cannot be any repeating numbers so a specific number
drawn already won't be drawn anymore in any future round. The program will also take note
of the number of rounds that have already passed. In each round, the program will automatically
mark the player's card by using the **cardmarker** function. It's highly recommended that the player
write down their numbers on a piece of paper and mark it themselves since the program won't show
the player's card being marked until after they finish the game.

In each round, the player also has a chance to call bingo by typing b into the program. If the
player decides to call bingo, the program will check if the marks on the player's card are showing
a specific pattern by using the **cardchecker** function. This specific function will also receive
the game mode so it can figure out if the player is playing on normal mode or jackpot mode. If the
marks on the card follow any winning pattern for normal mode, as described earlier, or if all the
numbers are marked for jackpot mode, the game ends, and the player's card will be shown on the
screen, along with all of the marks he or she was able to get during the game and the number of
rounds it took before he or she was able to call bingo.

Otherwise, an error message will pop up and the program will continue with the game. Since the
numbers being drawn are integers from 1-75 inclusive only, and no number is being drawn twice, the
game will also end if the player fails to call bingo correctly and all possible numbers have been
drawn already. Thus, the program will continue for a maximum of 75 rounds only. You can play this
game with a friend to see who can get bingo status in as few rounds as possible.
