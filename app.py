#
# XO Game
# In cmd xD
# By MrHora | Github page -> https://github.com/MrHooRa
#
import random
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
        print("\n\t\t\t\tWelcome To XO Game")
    mode = input(
        "\nGame mode:-\n\t[1]: player vs player\n\t[2]: player vs pc\n\t[3]: pc vs pc\n\t[4]: Exit\n> ")
    while not mode.isdigit() or int(mode) < 1 or int(mode) > 4:
        mode = input(
            "Game mode:-\n\t[1]: player vs player\n\t[2]: player vs pc\n\t[3]: pc vs pc\n\t[4]: Exit\n> ")
    if int(mode) == 1:
        game['setting']['mode'] = 1
    elif int(mode) == 2:
        game['setting']['mode'] = 2
    elif int(mode) == 3:
        game['setting']['mode'] = 3
        # DO NOT FORGET TO REMOVE UNDER THIS LINE!! #
        print("Sorry, but this feature doesn't work yet!")
        start()
        # DO NOT FORGET TO REMOVE ABOVE THIS LINE!! #
    elif int(mode) == 4:
        exit()

    player_1_nickname = input("\n\tPlayer 1 nickname: ")

    if game['setting']['mode'] == 1:
        player_2_nickname = input("\n\tPlayer 2 nickname: ")
    else:
        player_2_nickname = game['players']["player2"]

    if player_1_nickname != "":
        game['players']["player1"] = player_1_nickname
    if player_2_nickname != "" and int(mode) == 1:
        game['players']["player2"] = player_2_nickname
    game_board()
    choose_box(1, "X", 2)


def game_board():
    print("\n\t   {0}   |   {1}   |   {2}   \n\t-------|-------|-------\n\t   {3}   |   {4}   |   {5}   \n\t-------|-------|-------\n\t   {6}   |   {7}   |   {8}   ".format(
        game['box'][7], game['box'][8], game['box'][9], game['box'][4], game['box'][5], game['box'][6], game['box'][1], game['box'][2], game['box'][3]))


def restart():
    action = input("Play again? Yes[1] No[2]: ")
    if action == "Yes" or action == "yes" or action == "1":
        game['setting']['mode'] = 1
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
        box = input("\n\t{0} round ({1}): ".format(
            game['players']["player1"], "X"))
    elif player_id == 2:
        if game['setting']['mode'] == 1:
            box = input("\n\t{0} round ({1}): ".format(
                game['players']["player2"], "O"))
        elif game['setting']['mode'] == 2:
            box=0
            i = 1
            box_temp = []
            while i <= 9:
                if game['box'][i] == "-":
                    box_temp.append(i)
                i += 1
            if box_temp:
                box = random.choice(box_temp)
                box = str(box)

    while not box.isdigit() or box == "":
        if player_id == 1:
            box = input("\n\t{0} round ({1}): ".format(
                game['players']["player1"], "X"))
        elif player_id == 2:
            box = input("\n\t{0} round ({1}): ".format(
                game['players']["player2"], "O"))
    if 0 < int(box) < 10:
        if game['box'][int(box)] == "-":
            game['box'][int(box)] = player_letter
        else:
            print("\t\tYou can NOT choose this box! Try again!")
            choose_box(player_id, player_letter, next_player_id)
        game_board()
        check(next_player_id)
    else:
        print("\t\tYou can NOT choose this box! Try again!")
        choose_box(player_id, player_letter, next_player_id)

start(1)