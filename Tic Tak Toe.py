board = ["  " for i in range(9)]

def print_board():
    r1 = "| {} || {} | {} |".format(board[0],board[1],board[2])
    r2 = "| {} || {} | {} |".format(board[3],board[4],board[5])
    r3 = "| {} || {} | {} |".format(board[6],board[7],board[8])

    print()
    print(r1)
    print(r2)
    print(r3)

def player_move(icon):
    if icon =="X":
        num = 1
    elif icon == "O":
        num =2
    print("your turn Player {}".format(num))
    choice = int(input("Enter your choice(1-9): ").strip())
    if board[choice-1] =="  ":
        board[choice-1] = icon
    else:
        print()
        print("That space taken")

def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def if_draw():
    if "  " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("Player 1 Wins")
        break
    elif if_draw():
        print("Match Draws")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("Player 2 Wins")
        break
    elif if_draw():
        print("Match Draws")
        break
    
