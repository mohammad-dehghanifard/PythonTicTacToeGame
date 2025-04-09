from helpers import generate_board , game_status_check,game_controller

player = "X"
bot = "O"

board = list(range(1,10))


board = generate_board(board = board)

while game_status_check(board):
    move_index = int(input("choose your move(1-9) :"))
    moved , won = game_controller(board,move_index,player)

