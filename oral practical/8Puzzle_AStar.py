'''
Certainly! The Python code is an implementation of the A* algorithm for solving the 8-puzzle problem. Let's go through the code and understand its different components:

1. The code begins with function definitions for accepting the input puzzle configuration (`accept(n)`) and printing the puzzle board (`print_board(board, n)`).

2. The `find_space(Current, n)` function is used to find the position of the blank space (represented by '_') in the puzzle grid.

3. The `copy_current(Current)` function is used to create a copy of the current puzzle configuration.

4. The `shuffle(Current, brow_pos, bcol_pos, move_x, move_y)` function is used to move the blank space in a given direction (up, down, left, right) and create a new puzzle configuration. It checks if the move is within the puzzle grid boundaries and returns None if the move is out of range.

5. The `g_score(Node)` function calculates the g_score, which represents the number of nodes traversed from the start node to reach the current node.

6. The `h_score(Current, Goal, n)` function calculates the h_score, which represents the number of misplaced tiles by comparing the current state and the goal state of the puzzle.

7. The `f_score(Node, Goal, n)` function calculates the f_score, which is the sum of g_score and h_score for a given node.

8. The `move_gen(Node, Goal, n)` function generates the child nodes by moving the blank space in any of the four directions (up, down, left, right) and returns a list of child nodes.

9. The `goal_test(Current, Goal, n)` function checks if the goal configuration is reached by comparing the current configuration with the goal configuration.

10. The `sort(L)` function is used to sort the list L based on the f_score of each node.

11. The `play_game(Start, Goal, n)` function is the main driver function that initializes the A* algorithm. It sets up the initial node with the start configuration and the goal configuration. It creates the OPEN and CLOSED lists and iteratively explores nodes until the goal configuration is reached. It uses the helper functions defined above to perform the necessary operations.

12. Finally, the code accepts the board size (`n`), the start configuration (`Start`), and the goal configuration (`Goal`) from the user. It calls the `play_game()` function to start the A* algorithm and solve the 8-puzzle problem.

Note that the code assumes the input format for the puzzle configurations is a square grid of size `n x n`, where each tile is represented by a character or number. The blank space is represented by '_'. The start and goal configurations are entered by the user.
'''
def accept(n):
	puz = []
	for i in range(n):
		puz.append([val for val in input().split()])
	return puz

def print_board(board,n):
	for i in range(n):
		print()
		for j in range(n):
			print(board[i][j],end=' ')
	

#Find the position of blank space 
def find_space(Current,n):
		for blank_row_pos in range(n):
			for blank_col_pos in range(n):
				if Current[blank_row_pos][blank_col_pos]=='_':
					return blank_row_pos,blank_col_pos


#Copy the current node to new node for shuffling the blank space and create a new configuration
def copy_current(Current):
	temp=[]
	for i in range(len(Current)):
		row=[]
		for val in Current[i]:
			row.append(val)
			
		temp.append(row)
	
	return(temp)

#Move the blank space in given direction, if out of range return None
def shuffle(Current,brow_pos,bcol_pos,move_x,move_y):
	if move_x >= 0 and move_x < len(Current) and move_y >= 0 and move_y < len(Current):
		temp=[]
		temp=copy_current(Current)
		change=temp[move_x][move_y]
		temp[move_x][move_y]=temp[brow_pos][bcol_pos]
		temp[brow_pos][bcol_pos]=change
		return temp
	else:
		return None

#Function to calculate g_score: the number of nodes traversed from a start node to get to the current node
def g_score(Node):
	
	return Node[1] #Node=[Board,level,fscore]
	
	
#Function to calculate h_score: the number of misplaced tiles by comparing the current state and the goal state 
def h_score(Current,Goal,n):
	hscore=0
	for i in range(n):
		for j in range(n):
			if (Current[i][j] != Goal[i][j]) and (Current[i][j]!='_'):
				hscore +=1
	
	return hscore

#Function to calculate f_Score= g_score + h_Score
def f_score(Node,Goal,n):
	Current=Node[0]
	return g_score(Node) + h_score(Current,Goal,n)

#Generate the child nodes by moving the blank in any four direction (up,down,left,right)
def move_gen(Node,Goal,n):
	Current=Node[0]
	level=Node[1]
	fscore=0
	row,col=find_space(Current,n)
	move_positions=[[row,col-1],[row,col+1],[row-1,col],[row+1,col]] #left,right,up,down
	
	children=[] #List of child nodes of current node
	
	for move in move_positions:
		child=shuffle(Current,row,col,move[0],move[1])
		if child is not None:
			cNode=[child,0,0] #Dummy node for calculating f_Score
			fscore=f_score(cNode,Goal,n)
			
			Node=[child,level+1,fscore]
			children.append(Node)
	print("\n\n The Children ::",children)
	return children

#Function goal_test to see the goal configuration is reached
def goal_test(Current,Goal,n):
	if h_score(Current,Goal,n) == 0:
		return True
	else:
		return False

#Function to Sort OPEN based on f_score
def sort(L):
	L.sort(key = lambda x: x[2],reverse=False)
	return L 

#Function for starting the Game
def play_game(Start, Goal, n):
	#when game starts
	fscore=0 #fscore initialized to zero
	gscore=0 #gscore initialized to zero
	level=0 #the start configuration is root node s at level-0 of the state space tree
	
	Node=[Start,level,fscore]
	fscore=f_score(Node,Goal,n)
	
	#Every Node is [board configuration ,level,gscore]
	Node = [Start,level,fscore] # current node is Start node
	print("\nThe Node is=\n",Node)
	OPEN = [] #OPEN list as frontier
	CLOSED = [] #CLOSED as explored 
	OPEN.append(Node)
	levelcount=0
	
	#Explored the current node to reach to the Goal configuration
	while True:
		
		N=OPEN[0] #first node of open
		del OPEN[0] # delete first node of open
		
		Current=N[0] #Extract board configuration
		print("\n\n The current configuration is ::",Current)
		
		CLOSED.append(N)
		#if goal configuration is reached terminate
		if goal_test(Current,Goal,n) == True:
			print("\nGoal reached!!")
			print("CLOSED=",CLOSED)
			break
		
		CHILD=move_gen(N,Goal,n)
		#print("\n\n The CHILD is ::",CHILD)
		OPEN=[]
		for child in CHILD:
			OPEN.append(child)
		#sort the OPEN list based on fscore value of each node
		sort(OPEN) 
		

#Drive Code
n=int(input("Enter the board size:"))


print("\nEnter Start Configuration of board")
Start=accept(n)

print("\nEnter Goal Configuration of board")
Goal=accept(n)


play_game(Start, Goal, n)
