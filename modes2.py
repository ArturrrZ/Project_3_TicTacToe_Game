from art import logo, draw, x_won, o_won, end
import random
import time

row_1 = [
    " . ",
    " . ",
    " . ",
]
row_2 = [
    " . ",
    " . ",
    " . ",
]
row_3 = [
    " . ",
    " . ",
    " . ",
]
game_table = [row_1, row_2, row_3]
game_ui = f"{row_1[0]}|{row_1[1]}|{row_1[2]}\n___________\n" \
          f"{row_2[0]}|{row_2[1]}|{row_2[2]}\n___________\n" \
          f"{row_3[0]}|{row_3[1]}|{row_3[2]}\n___________\n"

# AI CHOICE TO PLAY
empty_box = ["11", "12", "13",
             "21", "22", "23",
             "31", "32", "33"]

list_of_choices = []


def reload_game_ui():
    global game_ui
    game_ui = f"{row_1[0]}|{row_1[1]}|{row_1[2]}\n___________\n" \
              f"{row_2[0]}|{row_2[1]}|{row_2[2]}\n___________\n" \
              f"{row_3[0]}|{row_3[1]}|{row_3[2]}\n___________\n"


def put(player):
    end = False
    while not end:

        choice = input("2 digits number (XY)\nX-stays for row. Y-for column:\n")
        try:
            if len(choice) == 2:
                if 0 < int(choice[0]) < 4 and 0 < int(choice[1]) < 4:
                    if choice in list_of_choices:
                        print("It's already taken")
                    else:
                        list_of_choices.append(choice)

                        row = int(choice[0]) - 1
                        column = int(choice[1]) - 1
                        empty_box.remove(choice)
                        # print(row, column)
                        game_table[row][column] = player
                        break
                else:
                    print("OUTSIDE OF RANGE\nYou can choose number from 1 to 3.\nPerfect Example: 31")
                    print("-------------------------------------------")
        except ValueError:
            print("I need just number!")


def check_winner():
    if row_1[0] == row_1[1] == " X " and row_1[0] == row_1[2] == " X ":
        return "x"
    if row_2[0] == row_2[1] == " X " and row_2[0] == row_2[2] == " X ":
        return "x"
    if row_3[0] == row_3[1] == " X " and row_3[0] == row_3[2] == " X ":
        return "x"
    if row_1[0] == row_2[0] == " X " and row_2[0] == row_3[0] == " X ":
        return "x"
    if row_1[1] == row_2[1] == " X " and row_2[1] == row_3[1] == " X ":
        return "x"
    if row_1[2] == row_2[2] == " X " and row_2[2] == row_3[2] == " X ":
        return "x"
    if row_1[0] == row_2[1] == " X " and row_2[1] == row_3[2] == " X ":
        return "x"
    if row_3[0] == row_2[1] == " X " and row_2[1] == row_1[2] == " X ":
        return "x"
    # --------
    if row_1[0] == row_1[1] == " O " and row_1[0] == row_1[2] == " O ":
        return "o"
    if row_2[0] == row_2[1] == " O " and row_2[0] == row_2[2] == " O ":
        return "o"
    if row_3[0] == row_3[1] == " O " and row_3[0] == row_3[2] == " O ":
        return "o"
    if row_1[0] == row_2[0] == " O " and row_2[0] == row_3[0] == " O ":
        return "o"
    if row_1[1] == row_2[1] == " O " and row_2[1] == row_3[1] == " O ":
        return "o"
    if row_1[2] == row_2[2] == " O " and row_2[2] == row_3[2] == " O ":
        return "o"
    if row_1[0] == row_2[1] == " O " and row_2[1] == row_3[2] == " O ":
        return "o"
    if row_3[0] == row_2[1] == " O " and row_2[1] == row_1[2] == " O ":
        return "o"


def is_draw():
    global list_of_choices
    if len(list_of_choices) == 9:
        return "yes"




def ai_play():
    global empty_box, list_of_choices
    pick = random.choice(empty_box)
    # print(pick)
    list_of_choices.append(pick)
    row = int(pick[0]) - 1
    column = int(pick[1]) - 1
    # print((row, column))
    empty_box.remove(pick)
    game_table[row][column] = " O "


def final_game():
    is_end = False
    while not is_end:
        reload_game_ui()
        print(game_ui)
        print("1st Player's turn ")
        put(player=" X ")
        check_winner()
        if is_draw() == "yes" and check_winner() != "x" and check_winner() != "o":
            print(draw)
            print("Final Table:")
            reload_game_ui()
            print(game_ui)
            is_end = True
            break
        if check_winner() == "x":
            print("Final Table:")
            reload_game_ui()
            print(game_ui)
            print(end)
            print("Player X won this game")
            break
        reload_game_ui()
        print(game_ui)
        print("2nd Player's turn ")
        put(player=" O ")
        check_winner()
        if check_winner() == "o":
            print("Final Table:")
            reload_game_ui()
            print(game_ui)
            print(end)
            print("Player O won this game")
            is_end = True


# ------------------MAIN GAME------------------------#



def is_ended():
    if is_draw() == "yes" and check_winner() != "x" and check_winner() != "o":
        print(draw)
        print("Final Table:")
        reload_game_ui()
        print(game_ui)

        return True
    if check_winner() == "x":
        print("Final Table:")
        reload_game_ui()
        print(game_ui)
        print(end)
        print("You won this game")
        return True
    elif check_winner() == "o":
        print("Final Table:")
        reload_game_ui()
        print(game_ui)
        print(end)
        print("AI won this game!")
        return True

play_one_more = False
aiplay = False

def ai():
    aip = False
    while not aip:
        reload_game_ui()
        print(game_ui)
        if random.randint(1, 2) == 2:
            print("AI turn first.")
            while not aiplay:

                print("Hmmm... Let's see")
                time.sleep(3)
                ai_play()
                check_winner()
                if is_ended() == True:
                    aip = True
                    break

                reload_game_ui()
                print(game_ui)
                print("Your turn!")
                put(player=" X ")
                check_winner()
                reload_game_ui()
                print(game_ui)
                if is_ended() == True:
                    aip = True
                    break

        else:
            print("Your turn first")
            while not aiplay:

                put(player=" X ")
                check_winner()
                if is_ended() == True:
                    aip = True
                    break
                reload_game_ui()
                print(game_ui)
                print("Hmmm... Let's see")
                time.sleep(3)
                ai_play()
                check_winner()
                if is_ended() == True:
                    aip = True
                    break
                reload_game_ui()
                print(game_ui)


print(logo)
print("Welcome to the Game!")

print(
    "Classic rules.\nThe first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
do_you_want_to_play = True
while do_you_want_to_play:
    ai_vs_frinds = input(
        "What mode would you like to play? \n1 - Friend vs friend\n2 - You vs Artificial Intelligence\nChoice: ")
    if ai_vs_frinds == "1":
        final_game()
    elif ai_vs_frinds == "2":
        ai()
    else:
        print("I dont have this mode yet")

    one_more = input("Do you want to play one more time? 'Y' for yes or any character for quit: ").title()
    if one_more != 'Y':
        print("Bye Bye!")
        do_you_want_to_play = False
    row_1 = [
        " . ",
        " . ",
        " . ",
    ]
    row_2 = [
        " . ",
        " . ",
        " . ",
    ]
    row_3 = [
        " . ",
        " . ",
        " . ",
    ]
    game_table = [row_1, row_2, row_3]
    game_ui = f"{row_1[0]}|{row_1[1]}|{row_1[2]}\n___________\n" \
              f"{row_2[0]}|{row_2[1]}|{row_2[2]}\n___________\n" \
              f"{row_3[0]}|{row_3[1]}|{row_3[2]}\n___________\n"

    list_of_choices = []
    empty_box = ["11", "12", "13",
                 "21", "22", "23",
                 "31", "32", "33"]