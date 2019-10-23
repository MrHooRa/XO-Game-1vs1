#
# XO Game
# By using array and some AI
#

players = {
    "player1": "Knight",
    "player2": "FireMaN"
}

game = {
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


def start(Type=0):
    if Type == 1:
        print("\n\t\t\t\tWelcome To XO Game\n")
    player_1_nickname = input("\n\tPlayer 1 nickname: ")
    player_2_nickname = input("\n\tPlayer 2 nickname: ")
    if player_1_nickname != "":
        players["player1"] = player_1_nickname
    if player_2_nickname != "":
        players["player2"] = player_2_nickname
    game_board()
    move(1)


def game_board():
    print("\n\t   {0}   |   {1}   |   {2}   \n\t-------|-------|-------\n\t   {3}   |   {4}   |   {5}   \n\t-------|-------|-------\n\t   {6}   |   {7}   |   {8}   ".format(
        game[7], game[8], game[9], game[4], game[5], game[6], game[1], game[2], game[3]))


def restart():
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
    else:
        print("Thank you for playing my game :D <3")
        exit


def when_win(player_id):
    if player_id == 1:
        print("\n\n\t {0} win!".format(players['player1']))
        print("\tI hope you enjoyed :D\n")
        again = 1
    if player_id == 2:
        print("\n\n\t {0} win!".format(players['player2']))
        print("\tI hope you enjoyed :D\n")
        again = 1
    if again == 1:
        restart()


def check(player, player_id=''):
    player_id = game[9] == "X" and game[6] == "X" and game[3] == "X" and 1 or player_id
    player_id = game[8] == "X" and game[5] == "X" and game[2] == "X" and 1 or player_id
    player_id = game[7] == "X" and game[4] == "X" and game[1] == "X" and 1 or player_id
    player_id = game[9] == "X" and game[8] == "X" and game[7] == "X" and 1 or player_id
    player_id = game[6] == "X" and game[5] == "X" and game[4] == "X" and 1 or player_id
    player_id = game[3] == "X" and game[2] == "X" and game[1] == "X" and 1 or player_id
    player_id = game[9] == "X" and game[5] == "X" and game[1] == "X" and 1 or player_id
    player_id = game[3] == "X" and game[5] == "X" and game[7] == "X" and 1 or player_id

    player_id = game[9] == "O" and game[6] == "O" and game[3] == "O" and 2 or player_id
    player_id = game[8] == "O" and game[5] == "O" and game[2] == "O" and 2 or player_id
    player_id = game[7] == "O" and game[4] == "O" and game[1] == "O" and 2 or player_id
    player_id = game[9] == "O" and game[8] == "O" and game[7] == "O" and 2 or player_id
    player_id = game[6] == "O" and game[5] == "O" and game[4] == "O" and 2 or player_id
    player_id = game[3] == "O" and game[2] == "O" and game[1] == "O" and 2 or player_id
    player_id = game[9] == "O" and game[5] == "O" and game[1] == "O" and 2 or player_id
    player_id = game[3] == "O" and game[5] == "O" and game[7] == "O" and 2 or player_id

    if player_id == 1 or player_id == 2:
        when_win(player_id)

    else:
        if game[1] != "-" and game[1] != "-" and game[2] != "-" and game[3] != "-" and game[4] != "-" and game[5] != "-" and game[6] != "-" and game[7] != "-" and game[8] != "-" and game[9] != "-":
            print("Game over!\n\n\tI hope you enjoyed :D")
            restart()
        else:
            move(player)


def choose_box(player_id, player_letter, player_id_next_round):
    if player_id == 1:
        box = input("\n\t{0} round ({1}): ".format(players["player1"], "X"))
    elif player_id == 2:
        box = input("\n\t{0} round ({1}): ".format(players["player2"], "O"))

    if box.isdigit() and box != "":
        box = int(box)
    else:
        print("\t\tTry again!")
        choose_box(player_id, player_letter, player_id_next_round)
    if 0 < box < 10:
        if game[box] == "-":
            game[box] = player_letter
        else:
            print("\t\tYou can NOT choose this box!")
            choose_box(player_id, player_letter, player_id_next_round)
    game_board()
    check(player_id_next_round)


def move(player):
    if player == 1:
        choose_box(player, "X", 2)
    elif player == 2:
        choose_box(player, "O", 1)


# Start form here!
start(1)
