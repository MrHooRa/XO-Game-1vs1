#
# XO Game
# By using array and some AI
#

players = {
    "player1": "Player 1",
    "player2": "Player 2"
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
    players["player1"] = input("\n\tPlayer 1 nickname: ")
    players["player2"] = input("\n\tPlayer 2 nickname: ")


def game_board():
    print("\n\t|=======================|\n\t|   {0}   |   {1}   |   {2}   |\n\t|-------|-------|-------|\n\t|   {3}   |   {4}   |   {5}   |\n\t|-------|-------|-------|\n\t|   {6}   |   {7}   |   {8}   |\n\t|=======================|".format(
        game[7], game[8], game[9], game[4], game[5], game[6], game[1], game[2], game[3]))


def check(player):
    if game[1] != "-" and game[1] != "-" and game[2] != "-" and game[3] != "-" and game[4] != "-" and game[5] != "-" and game[6] != "-" and game[7] != "-" and game[8] != "-" and game[9] != "-":
        print("Game over!")
    else:
        if game[9] == "X" and game[6] == "X" and game[3] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[8] == "X" and game[5] == "X" and game[2] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[7] == "X" and game[4] == "X" and game[1] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[9] == "X" and game[8] == "X" and game[7] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[6] == "X" and game[5] == "X" and game[4] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[3] == "X" and game[2] == "X" and game[1] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[3] == "X" and game[2] == "X" and game[1] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[9] == "X" and game[5] == "X" and game[1] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[3] == "X" and game[5] == "X" and game[7] == "X":
            print("\n\n\t\t {0} win!\n\n".format(players['player1']))
            game["start"] = 0
        if game[9] == "O" and game[6] == "O" and game[3] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[8] == "O" and game[5] == "O" and game[2] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[7] == "O" and game[4] == "O" and game[1] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[9] == "O" and game[8] == "O" and game[7] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[6] == "O" and game[5] == "O" and game[4] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[3] == "O" and game[2] == "O" and game[1] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[3] == "O" and game[2] == "O" and game[1] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[9] == "O" and game[5] == "O" and game[2] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game[3] == "O" and game[5] == "O" and game[7] == "O":
            print("\n\n\t\t {0} win!\n\n".format(players['player2']))
            game["start"] = 0
        if game["start"] == 0:
            print("I hope you enjoyed :D")
        else:
            move(player)


def move(player):
    if player == 1:
        if game['start'] == 1:
            player_choose = input("\n\t{0} round: ".format(players['player1']))
            player_choose = int(player_choose)
            if player_choose < 10:
                if game[player_choose]:
                    game[player_choose] = 'X'
            game_board()
            check(2)
    if player == 2:
        if game['start'] == 1:
            player_choose = input("\n\t{0} round: ".format(players['player2']))
            player_choose = int(player_choose)
            if player_choose < 10:
                if game[player_choose]:
                    game[player_choose] = 'O'
            game_board()
            check(1)


if game['start'] == 0:
    print("\n\t\tWelcome To start please choose which box you want!\n")
    start()
    game_board()
    game["start"] = 1
    move(1)