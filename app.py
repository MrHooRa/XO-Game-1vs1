#
# XO Game
# By using array and some AI
#

game = {
    'players': {
        "player1": "Knight",
        "player2": "FireMaN"
    },
    'setting': {
        'mode': 1
    },
    'box': {
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
}


def start(Type=0):
    if Type == 1:
        print("\n\t\t\t\tWelcome To XO Game\n")
    player_1_nickname = input("\n\tPlayer 1 nickname: ")
    player_2_nickname = input("\n\tPlayer 2 nickname: ")
    if player_1_nickname != "":
        game['players']["player1"] = player_1_nickname
    if player_2_nickname != "":
        game['players']["player2"] = player_2_nickname
    game_board()
    choose_box(1, "X", 2)


def game_board():
    print("\n\t   {0}   |   {1}   |   {2}   \n\t-------|-------|-------\n\t   {3}   |   {4}   |   {5}   \n\t-------|-------|-------\n\t   {6}   |   {7}   |   {8}   ".format(
        game['box'][7], game['box'][8], game['box'][9], game['box'][4], game['box'][5], game['box'][6], game['box'][1], game['box'][2], game['box'][3]))


def restart():
    action = input("Play again? Yes[1] No[2]: ")
    if action == "Yes" or action == "yes" or action == "1":
        game['box'][1] = '-'
        game['box'][2] = '-'
        game['box'][3] = '-'
        game['box'][4] = '-'
        game['box'][5] = '-'
        game['box'][6] = '-'
        game['box'][7] = '-'
        game['box'][8] = '-'
        game['box'][9] = '-'
        start()
    else:
        print("Thank you for playing my game :D <3")
        exit()


def when_win(player_id):
    if player_id == 1:
        print("\n\n\t {0} win!".format(game['players']['player1']))
        print("\tI hope you enjoyed :D\n")
        again = 1
    if player_id == 2:
        print("\n\n\t {0} win!".format(game['players']['player2']))
        print("\tI hope you enjoyed :D\n")
        again = 1
    if again == 1:
        restart()


def check(player, player_id=''):
    player_id = game['box'][9] == "X" and game['box'][6] == "X" and game['box'][3] == "X" and 1 or player_id
    player_id = game['box'][8] == "X" and game['box'][5] == "X" and game['box'][2] == "X" and 1 or player_id
    player_id = game['box'][7] == "X" and game['box'][4] == "X" and game['box'][1] == "X" and 1 or player_id
    player_id = game['box'][9] == "X" and game['box'][8] == "X" and game['box'][7] == "X" and 1 or player_id
    player_id = game['box'][6] == "X" and game['box'][5] == "X" and game['box'][4] == "X" and 1 or player_id
    player_id = game['box'][3] == "X" and game['box'][2] == "X" and game['box'][1] == "X" and 1 or player_id
    player_id = game['box'][9] == "X" and game['box'][5] == "X" and game['box'][1] == "X" and 1 or player_id
    player_id = game['box'][3] == "X" and game['box'][5] == "X" and game['box'][7] == "X" and 1 or player_id

    player_id = game['box'][9] == "O" and game['box'][6] == "O" and game['box'][3] == "O" and 2 or player_id
    player_id = game['box'][8] == "O" and game['box'][5] == "O" and game['box'][2] == "O" and 2 or player_id
    player_id = game['box'][7] == "O" and game['box'][4] == "O" and game['box'][1] == "O" and 2 or player_id
    player_id = game['box'][9] == "O" and game['box'][8] == "O" and game['box'][7] == "O" and 2 or player_id
    player_id = game['box'][6] == "O" and game['box'][5] == "O" and game['box'][4] == "O" and 2 or player_id
    player_id = game['box'][3] == "O" and game['box'][2] == "O" and game['box'][1] == "O" and 2 or player_id
    player_id = game['box'][9] == "O" and game['box'][5] == "O" and game['box'][1] == "O" and 2 or player_id
    player_id = game['box'][3] == "O" and game['box'][5] == "O" and game['box'][7] == "O" and 2 or player_id

    if player_id == 1 or player_id == 2:
        when_win(player_id)

    else:
        if game['box'][1] != "-" and game['box'][1] != "-" and game['box'][2] != "-" and game['box'][3] != "-" and game['box'][4] != "-" and game['box'][5] != "-" and game['box'][6] != "-" and game['box'][7] != "-" and game['box'][8] != "-" and game['box'][9] != "-":
            print("Game over!\n\n\tI hope you enjoyed :D")
            restart()
        else:
            if player == 1:
                choose_box(1, "X", 2)
            elif player == 2:
                choose_box(2, "O", 1)


def choose_box(player_id, player_letter, next_player_id):
    if player_id == 1:
        box = input("\n\t{0} round ({1}): ".format(game['players']["player1"], "X"))
    elif player_id == 2:
        box = input("\n\t{0} round ({1}): ".format(game['players']["player2"], "O"))

    if box.isdigit() and box != "":
        box = int(box)
    else:
        print("\t\tTry again!")
        choose_box(player_id, player_letter, next_player_id)
    if 0 < box < 10:
        if game['box'][box] == "-":
            game['box'][box] = player_letter
        else:
            print("\t\tYou can NOT choose this box! Try again!")
            choose_box(player_id, player_letter, next_player_id)
        game_board()
        check(next_player_id)
    else:
        print("\t\tYou can NOT choose this box! Try again!")
        choose_box(player_id, player_letter, next_player_id)


# Start form here!
start(1)
