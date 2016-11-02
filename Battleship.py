from random import randint
board = [] #create an empty list

for n in range (1,11): 
    board.append(["O"]*10) #adds a list of 10 "O"s WITHIN the board list, repeated 10 times by the loop
    
def print_board(lst): #prints the lists within the board list on a new line for clarity
    for row in lst:
        print ("  ".join(row)) #use join method on '  ' string to combine the items in the list, for prettiness

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(1, len(board)) #returns random integer with a low of 1 and high of len(board), which is 10
def random_col(board):
    return randint(1, len(board[0])) #returns random integer with a low of 1 and high of len(board[0]), which is also 10

ship_row = random_row(board) #set variables equal to result of random integer function
ship_col = random_col(board)

#Useful for debugging, this displays the answer when uncommented
#print (ship_row)
#print (ship_col)

for turn in range(1,5): #loop the following code 4 times
	print ("Turn", turn) #print the number of the loop as a turn

	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Col: "))

	if guess_row == ship_row or guess_row == ship_row+1 or guess_row == ship_row-1 and guess_col == ship_col or guess_col == ship_col+1 or guess_col == ship_col-1:
		print ("Congratulations! You sank my battleship!")
		board[guess_row-1][guess_col-1] = "S"
		print_board(board)
		break #end the game when the ship is sunk
	else:
		if (guess_row < 1 or guess_row > 10) or (guess_col < 1 or guess_col > 10):
			print ("Oops, that's not even in the ocean.")
		elif(board[guess_row][guess_col] == "X"): 
			print ("You guessed that one already.")
		else:
			print ("You missed my battleship!")
			board[guess_row-1][guess_col-1] = "X" #incorrect guesses turn 'O's into 'X's, can be checked in the elif statement after at least 1 loop
		if turn ==4:
			print ("Game Over")
			break
	print_board(board) 
        
