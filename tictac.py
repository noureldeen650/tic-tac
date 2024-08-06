player1 = ""
player2 = ""
player_input = ""
block = []
def start_game():

    for i in range(9):
        block.insert(i, "#")
    print("Welcome to Tic Tac Toe")
    assign_players()

def assign_players():
    global player1, player2
    player_input = input("Choose X or O: ").upper()
    if player_input == "X":
        player1 = 'X'
        player2 = 'O'
        choose_blocks()
    elif player_input == "O":
        player1 = 'O'
        player2 = 'X'
        choose_blocks()
    else:
        print("Invalid choice, please choose again")
        assign_players()

def choose_blocks():
    print("Game started!")
    current_player = player1
    for i in range(9):
        display()
        choice = input(f"Player {current_player} please choose a block from 0 to 8: ")
        if choice.isdigit():
            choice = int(choice)
            if choice < 9 and choice >= 0:
                if block[choice] == "#":
                    block[choice] = current_player
                    if check_winner():
                        display()
                        print(f"Player {current_player} wins!")
                        return
                    current_player = player2 if current_player == player1 else player1
                else:
                    print("Block already taken, choose again")
            else:
                print("Block number invalid, choose again")
        else:
            print("Please choose a number, choose again")
    print("It's a draw!")
    display()

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in winning_combinations:
        if block[a] == block[b] == block[c] != "#":
            return True
    return False

def display():
    print(block[0] + "  " + block[1] + "  " + block[2])
    print(block[3] + "  " + block[4] + "  " + block[5])
    print(block[6] + "  " + block[7] + "  " + block[8])
    print('\n')



start_game()



