#
# XO Game
# By using array and some AI
#

players = {
    "player1": "Knight",
    "player2": "FireMaN"
}

game = {
    "start": 0,
    1: "-",
    2: "-",
    3: "-",
    4: "-",
    5: "-",
    6: "-",
    7: "-",
    8: "-",
    9: "-"
}


def start():
    player_1_nickname = input("\n\tPlayer 1 nickname: ")
    player_2_nickname = input("\n\tPlayer 2 nickname: ")
    if player_1_nickname != "":
        players["player1"] = player_1_nickname
    if player_2_nickname != "":
        players["player2"] = player_2_nickname


def game_board():
    print("\n\t|=======================|\n\t|   {0}   |   {1}   |   {2}   |\n\t|-------|-------|-------|\n\t|   {3}   |   {4}   |   {5}   |\n\t|-------|-------|-------|\n\t|   {6}   |   {7}   |   {8}   |\n\t|=======================|".format(
        game[7], game[8], game[9], game[4], game[5], game[6], game[1], game[2], game[3]))


def check(player):
    
    if game[9] == "X" and game[6] == "X" and game[3] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[8] == "X" and game[5] == "X" and game[2] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[7] == "X" and game[4] == "X" and game[1] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[9] == "X" and game[8] == "X" and game[7] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[6] == "X" and game[5] == "X" and game[4] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[3] == "X" and game[2] == "X" and game[1] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[3] == "X" and game[2] == "X" and game[1] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[9] == "X" and game[5] == "X" and game[1] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[3] == "X" and game[5] == "X" and game[7] == "X":
        print("\n\n\t\t {0} win!\n\n".format(players['player1']))
        game["start"] = 2
    if game[9] == "O" and game[6] == "O" and game[3] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[8] == "O" and game[5] == "O" and game[2] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[7] == "O" and game[4] == "O" and game[1] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[9] == "O" and game[8] == "O" and game[7] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[6] == "O" and game[5] == "O" and game[4] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[3] == "O" and game[2] == "O" and game[1] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[3] == "O" and game[2] == "O" and game[1] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[9] == "O" and game[5] == "O" and game[2] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game[3] == "O" and game[5] == "O" and game[7] == "O":
        print("\n\n\t\t {0} win!\n\n".format(players['player2']))
        game["start"] = 2
    if game["start"] == 2:
        print("I hope you enjoyed :D")
        action = input("Play again? Yes[1] No[2]: ")
        if action == "Yes" or action == "yes" or action == "1":
            game[1] = '-'
            game[2] = '-'
            game[3] = '-'
            game[4] = '-'
            game[5] = '-'
            game[6] = '-'
            game[7] = '-'
            game[8] = '-'
            game[9] = '-'
            start()
            game_board()
            game["start"] = 1
            move(1)
        else:
            print("Thank you for playing my game :D <3")
            exit
    if game['start'] != "0":
        if game[1] != "-" and game[1] != "-" and game[2] != "-" and game[3] != "-" and game[4] != "-" and game[5] != "-" and game[6] != "-" and game[7] != "-" and game[8] != "-" and game[9] != "-":
            print("Game over!")
            print("\n\n\tI hope you enjoyed :D")
            action = input("\nPlay again? Yes[1] No[2]: ")
            if action == "Yes" or action == "yes" or action == "1":
                game[1] = '-'
                game[2] = '-'
                game[3] = '-'
                game[4] = '-'
                game[5] = '-'
                game[6] = '-'
                game[7] = '-'
                game[8] = '-'
                game[9] = '-'
                start()
                game_board()
                game["start"] = 1
                move(1)
            else:
                print("Thank you for playing my game :D <3")
                exit
        else:
            move(player)


def move(player):
    if player == 1:
        if game['start'] == 1:
            box = input("\n\t{0} round (X): ".format(players['player1']))
            if box.isdigit() and box != "":
                box = int(box)
            else:
                print("\t\tTry again!")
                move(player)
            if box < 10:
                if game[box] == "-":
                    game[box] = 'X'
                else:
                    print("\t\tYou can NOT choose this box!")
                    move(player)
            game_board()
            check(2)
    if player == 2:
        if game['start'] == 1:
            box = input("\n\t{0} round (O): ".format(players['player2']))
            if box.isdigit() and box != "":
                box = int(box)
            else:
                print("\t\tTry again!")
                move(player)
            if box < 10:
                if game[box] == "-":
                    game[box] = 'O'
                else:
                    print("\t\tYou can NOT choose this box!")
                    move(player)
            game_board()
            check(1)


# if game['start'] == 0:
#     print("\n\t\t\t\tWelcome To XO Game\n")
#     start()
#     game_board()
#     game["start"] = 1
#     move(1)


array = {
    1: True,
    2: True,
    3: False
}

end = game[9] == "-" and game[6] == "-" and game[3] == "-" and "Hello World :D" or "Nothing"
print(end)