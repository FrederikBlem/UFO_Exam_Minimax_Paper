computer, human = 'x', 'o'
gameRoundNum = 1
isGameOver = False

# This function returns true if there are moves left on the board
def canMove(board) : 

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False

# Evaluate checks for victory conditions. 
# Returns 10 for X, 0 for TIE or -10 for O
def evaluate(board) : 

	# Checking the Rows for a victory by X or O. 
	for row in range(3) :	 
		if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :	 
			if (board[row][0] == computer) :
				return 10
			elif (board[row][0] == human) :
				return -10

	# Checking the Columns for a victory by X or O.
	for col in range(3) :
	
		if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
		
			if (board[0][col] == computer) : 
				return 10
			elif (board[0][col] == human) :
				return -10

	# Checking the Diagonals for a victory by X or O.
	if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
	
		if (board[0][0] == computer) :
			return 10
		elif (board[0][0] == human) :
			return -10

	if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
	
		if (board[0][2] == computer) :
			return 10
		elif (board[0][2] == human) :
			return -10

	# If no victory is found, return 0.
	return 0

# The minimax function iterates all the moves the
# game can go through and returns the best value move
def minimax(board, depth, isMax) : 
	score = evaluate(board)

    # In the case the Maximizer has won.
	if (score == 10) : 
		return score

	# In the case the Minimizer has won.
	if (score == -10) :
		return score

	# In the case that there are no moves left and no winner - TIE.
	if (canMove(board) == False) :
		return 0

	# In the case that it's the Maximizer's move (computer)
	if (isMax) :	 
		best = -1000

		# Check if the cells are empty one by one and make a move
		for i in range(3) :		 
			for j in range(3) :
			
				
				if (board[i][j]=='_') :
				
					board[i][j] = computer 
                    
                    # Call the function recursively, updating the value 
                    # of 'best' to be the BIGGEST value found.
					best = max( best, minimax(board, depth + 1, not isMax))

					# Clean up the board by erasing the move. 
					board[i][j] = '_'
		return best

	# In the case that it's the Minimizer's move 
    # (we use this to understand human's best move)
	else :
		best = 1000

		# Check if the cells are empty one by one and make a move
		for i in range(3) :		 
			for j in range(3) :
			
				if (board[i][j] == '_') :
				
					board[i][j] = human 

					# Call the function recursively, updating the value 
                    # of 'best' to be the SMALLEST value found.
					best = min(best, minimax(board, depth + 1, not isMax))

					# Clean up the board by erasing the move.
					board[i][j] = '_'
		return best

# This will return the best possible move for the computer 
def findBestMove(board) : 
	bestVal = -1000
	bestMove = (-1, -1) 

	# Iterate through all the cells on the board and then 
    # evaluate minimax function for the empty cells. 
    # And then return the cell with the best value. 
	for i in range(3) :	 
		for j in range(3) :
		
			# Check if the cells are empty one by one and make a move
			if (board[i][j] == '_') : 
			
				board[i][j] = computer

                # Run the minimax function to evaluate this move.
				moveVal = minimax(board, 0, False) 

				# Clean up the board by erasing the move.
				board[i][j] = '_'

				# If the current move is more valuable than bestVal, 
                # then update bestMove
				if (moveVal > bestVal) :			 
					bestMove = (i, j)
					bestVal = moveVal

	print("The value of the best Move is :", bestVal)
	print()
    
	return bestMove

def printBoard():
    print("------------------------------------")
    print(board[0])
    print(board[1])
    print(board[2])
    print("------------------------------------")


def playRound() :
    if (gameRoundNum % 2 != 0):
        print("MOVE ", gameRoundNum, ", COMPUTER")
        
        bestMove = findBestMove(board) 

        print("The Optimal Move is :") 
        print("ROW:", bestMove[0], " COL:", bestMove[1])
        board[bestMove[0]][bestMove[1]] = 'x'
    else:
        print("MOVE ", gameRoundNum, ", HUMAN")
        
        validMove = False # Meant to check if Human plays a valid move
        
        while(validMove == False):
            rowHuman = int(input('Choose Row 0-2: '))
            colHuman = int(input('Choose Column 0-2: '))
            
            if(board[rowHuman][colHuman] == '_'):
                validMove = True
            else:
                print("Invalid move! The space is occupied.")
                print("Here's the board again: ")
                printBoard()

        board[rowHuman][colHuman] = 'o'   
    
    printBoard()

# Initialize board.
board = [
	[ '_', '_', '_' ], 
	[ '_', '_', '_' ], 
	[ '_', '_', '_' ] 
]


while(isGameOver == False and canMove(board)):
    
    playRound()
    score = evaluate(board)
    #print("The score is: ", score)
    
    if(score == 0 and canMove(board) == False):  
        print("TIE... NOT BAD, HUMAN")
        isGameOver = True
    elif(score == 0):  
        gameRoundNum += 1
    elif(score == -10):
        print("HUMAN WINS - MUST'VE CHEATED!")
        isGameOver = True
    elif(score == 10):
        print("COMPUTER WINS AGAIN - AS EXPECTED")
        isGameOver = True
    else:
        print("How did we get to this score here?: ", score)
        isGameOver = True
        