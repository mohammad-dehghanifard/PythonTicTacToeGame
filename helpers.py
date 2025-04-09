
winner_rules = ((0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(8,4,0),(3,4,5),(6,7,8))

def generate_board(board : list) :
    x = 1
    for i in board :
        end = " "
        if x % 3 == 0 :
            end = "\n"
        if i == "X" :
            print(f"[{i}]" , end = end)
        elif i == "O" :
            print(f"[{i}]" , end = end)
        else:
            print(f"[{i - 1}]" , end = end)
        x += 1

def game_status_check(board : list) :
    return board.count("X") + board.count("O") != 9

def can_move(board : list , move_index : int) :
    if move_index in range(1, 10) and isinstance(board[move_index - 1], int):
        return True
    else :
        return False

def win_check(board : list,player_selected_index : tuple) :
    win = True
    for wins_tuple in winner_rules :
        for j in wins_tuple :
            if board[j] != player_selected_index :
                win = False
                break
            if win :
                break
    return win

def game_controller(board : list,player : int,move_index : int,undo : bool = False) :
    if can_move(board, move_index):
        board[move_index - 1] = player
        win = win_check(board,player)
        if undo :
            board[move_index - 1] = move_index
            return True,win
        return False,False