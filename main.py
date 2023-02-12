board = {
   1: "_",
   2: "_",
   3: "_",
   4: "_",
   5: "_",
   6: "_",
   7: "_",
   8: "_",
   9: "_",
}
 
 
def print_board():
   print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print(f"{board[1]}  |  {board[2]}  |  {board[3]}")
   print(f"--------------")
   print(f"{board[4]}  |  {board[5]}  |  {board[6]}")
   print(f"--------------")
   print(f"{board[7]}  |  {board[8]}  |  {board[9]}")
 
 
def check_winner():
   return ((board[1] == board[2] == board[3] == turn) or  # top row
           (board[4] == board[5] == board[6] == turn) or  # middle row
           (board[7] == board[8] == board[9] == turn) or  # bottom row
           (board[1] == board[4] == board[7] == turn) or  # first column
           (board[2] == board[5] == board[8] == turn) or  # second column
           (board[3] == board[6] == board[9] == turn) or  # third column
           (board[1] == board[5] == board[9] == turn) or  # left diagonal
           (board[3] == board[5] == board[7] == turn))    # right diagonal
 
 
def check_tie():
   return board[1] != "_" and board[2] != "_" and board[3] != "_" and \
          board[4] != "_" and board[5] != "_" and board[6] != "_" and \
          board[7] != "_" and board[8] != "_" and board[9] != "_"
 
 
turn = "X"
game_over = False
 
while not game_over:
   print_board()
 
   place = int(input(f"{turn}'s turn: "))
   while board[place] != "_":
       place = int(input(f"Whoops! That place is already taken, {turn}. Try that again: "))
 
   board[place] = turn
 
   if check_winner():
       print_board()
       print(f"Good job! {turn} won!")
       game_over = True
   if check_tie():
       print_board()
       print("Woah, it's a tie.")
       game_over = True
 
   if turn == "X":
       turn = "O"
   elif turn == "O":
       turn = "X"
