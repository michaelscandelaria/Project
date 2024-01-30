from tabulate import tabulate
import random

def main():
    print("\nGood evening, ladies and gentlemen! The gamemaster welcomes you to the 75-ball Bingo Games!\n")
    startgame = "no"
    customize = "r"
    while startgame == "no":
        print ("\nIf you want to customize your own bingo card, type in c")
        customize = str(input("Otherwise, the gamemaster will generate one for you. ")).strip().lower()

        if customize == "c":
            card = [["B", "I", "N", "G", "O"],
                    ["A1", "A2", "A3", "A4", "A5"],
                    ["B1", "B2", "B3", "B4", "B5"],
                    ["C1", "C2", "C3", "C4", "C5"],
                    ["D1", "D2", "D3", "D4", "D5"],
                    ["E1", "E2", "E3", "E4", "E5"]]
            values = []
            print("\nSo, you want to go through the trouble of customizing your own card...")
            print("The gamemaster respects your decision. Here are just some ground rules you need to follow:")
            print("1. All numbers in the first column (leftmost) should be numbers from 1-15")
            print("2. All numbers in the second column should be numbers from 16-30")
            print("3. All numbers in the third column (except for C3) should be numbers from 31-45")
            print("4. All numbers in the fourth column should be numbers from 46-60")
            print("5. All numbers in the fifth column (rightmost) should be numbers from 61-75")
            print("6. You cannot have any repeating numbers in your card\n")
            print(tabulate(card, tablefmt="double_grid"))
            print()

            val = 0
            for outerlist in range(1, 6):
                for innerlist in range(0, 5):
                    while True:

                        if card[outerlist][innerlist] == "C3":
                            break

                        try:
                            val = int(input(f"What should I put in position {card[outerlist][innerlist]}? "))
                            if val in values:
                                print("You cannot repeat numbers!", end=" ")
                            elif initializer(innerlist, val):
                                card[outerlist][innerlist] = val
                                values.append(val)
                                break
                            else:
                                raise ValueError

                        except ValueError:
                            print("Please pick a positive integer within the acceptable range only!", end=" ")

        else:
            card = [["B", "I", "N", "G", "O"],
                    ["A1", "A2", "A3", "A4", "A5"],
                    ["B1", "B2", "B3", "B4", "B5"],
                    ["C1", "C2", "C3", "C4", "C5"],
                    ["D1", "D2", "D3", "D4", "D5"],
                    ["E1", "E2", "E3", "E4", "E5"]]
            values = []

            for outerlist in range(1, 6):
                for innerlist in range(0, 5):
                    while True:
                        thisnum = random.randint(1, 75)
                        if card[outerlist][innerlist] == "C3":
                            break
                        elif ((initializer(innerlist, thisnum)) and (thisnum not in values)):
                            card[outerlist][innerlist] = thisnum
                            values.append(thisnum)
                            break

        print()
        print(tabulate(card, tablefmt="double_grid"))
        startgame = input("Are you sure you want to proceed with this card? Type no to change your card. ")
        startgame = str(startgame).strip().lower()

    print()
    print("Hey! Make sure you write down your numbers on a piece of paper before you start the game!")
    print("You won't be able to see your card being marked until after you finish the game.")
    print()
    print("There are 2 modes of gameplay for this bingo game. In normal mode, you have to mark all of the")
    print("numbers in any row, column, or diagonal. In jackpot mode, you have to mark all of the numbers in")
    print("your entire card. The gamemaster suggests you try normal mode first if you want a warm-up round.")
    print("Take note as well that the C3 position on your card is a free spot, meaning you can automatically")
    print("mark it even before the game starts. You can only mark a number on your card, by the way, if the")
    print("gamemaster drew that particular number already in the current round or in any previous round. So...")
    print("If you want the jackpot experience, I dare you to go ahead and type in j")
    mode = str(input("Otherwise, the game will default to normal mode. ")).strip().lower()
    print()
    card[3][2] = "X"
    allgameval = []
    round = 0
    bingo = False
    for oneval in range(1, 76):
        allgameval.append(oneval)

    while ((bingo == False) and (len(allgameval) > 0)):
        round = round + 1
        thisgameval = random.choice(allgameval)
        allgameval.remove(thisgameval)
        card = cardmarker(card, thisgameval)
        b = str(input(f"Round {round}! The gamemaster drew the number {thisgameval}. Type in b if you want to call bingo. "))
        b = b.strip().lower()

        if b == "b":
            if (cardchecker(card, mode)):
                bingo = True
            else:
                print("Are you sure about that? The gamemaster thinks otherwise.\n")

    if ((bingo == True) and (mode != "j")):
        print()
        print(tabulate(card, tablefmt="double_grid"))
        print(f"The gamemaster congratulates you for your achievement! You achieved the coveted bingo in {round} rounds.\n")
    elif ((bingo == True) and (mode == "j")):
        print()
        print(tabulate(card, tablefmt="double_grid"))
        print(f"Wow! The gamemaster is amazed at your skill! You got the jackpot in {round} rounds.\n")
    else:
        print()
        print(tabulate(card, tablefmt="double_grid"))
        print("The gamemaster offers you his condolences. Unfortunately, you weren't able to achieve the coveted bingo.")
        print("Or maybe you just weren't paying attention... keep your head in the game next time!\n")

def initializer (innerlist, val):
    match innerlist:
        case 0:
            if 1 <= val <= 15:
                return True
            else:
                return False

        case 1:
            if 16 <= val <= 30:
                return True
            else:
                return False

        case 2:
            if 31 <= val <= 45:
                return True
            else:
                return False

        case 3:
            if 46 <= val <= 60:
                return True
            else:
                return False

        case 4:
            if 61 <= val <= 75:
                return True
            else:
                return False

def cardmarker(card, thisgameval):
    if 1 <= thisgameval <= 15:
        for i in range(1, 6):
            if str(card[i][0]) == str(thisgameval):
                card[i][0] = "X"

    elif 16 <= thisgameval <= 30:
        for i in range(1, 6):
            if str(card[i][1]) == str(thisgameval):
                card[i][1] = "X"

    elif 31 <= thisgameval <= 45:
        for i in range(1, 6):
            if str(card[i][2]) == str(thisgameval):
                card[i][2] = "X"

    elif 46 <= thisgameval <= 60:
        for i in range(1, 6):
            if str(card[i][3]) == str(thisgameval):
                card[i][3] = "X"

    else:
        for i in range(1, 6):
            if str(card[i][4]) == str(thisgameval):
                card[i][4] = "X"

    return card

def cardchecker(card, mode):
    xspots = []
    for outerlist in range(1, 6):
        for innerlist in range(0, 5):

            if str(card[outerlist][innerlist]) == "X":
                xspots.append(f"{outerlist}-{innerlist}")

    if ((mode == "j") and (len(xspots) == 25)):
        return True
    elif ((mode == "j") and (len(xspots) < 25)):
        return False
    elif {"1-0", "1-1", "1-2", "1-3", "1-4"}.issubset(xspots):
        return True
    elif {"2-0", "2-1", "2-2", "2-3", "2-4"}.issubset(xspots):
        return True
    elif {"3-0", "3-1", "3-2", "3-3", "3-4"}.issubset(xspots):
        return True
    elif {"4-0", "4-1", "4-2", "4-3", "4-4"}.issubset(xspots):
        return True
    elif {"5-0", "5-1", "5-2", "5-3", "5-4"}.issubset(xspots):
        return True
    elif {"1-0", "2-0", "3-0", "4-0", "5-0"}.issubset(xspots):
        return True
    elif {"1-1", "2-1", "3-1", "4-1", "5-1"}.issubset(xspots):
        return True
    elif {"1-2", "2-2", "3-2", "4-2", "5-2"}.issubset(xspots):
        return True
    elif {"1-3", "2-3", "3-3", "4-3", "5-3"}.issubset(xspots):
        return True
    elif {"1-4", "2-4", "3-4", "4-4", "5-4"}.issubset(xspots):
        return True
    elif {"1-0", "2-1", "3-2", "4-3", "5-4"}.issubset(xspots):
        return True
    elif {"1-4", "2-3", "3-2", "4-1", "5-0"}.issubset(xspots):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
