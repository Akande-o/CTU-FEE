import copy
from game_board import GameBoard

class MyPlayer():
    '''A player instance implemented by using alpha-beta prunning with minimax''' # TODO a short description of your player

    def __init__(self, my_color,opponent_color, board_size):
        '''Initialising the different attributes of the player instance'''
        self.name = 'olasoolu' #TODO: fill in your username
        self.my_color = my_color      # to identify my player
        self.opponent_color = opponent_color    # to identify my opponent
        self.board_size = board_size        # The size of the board
        self.min_value = -100       # the minimum possible evaluation output
        self.max_value = 300   # the maximum possible evaluation
    def move(self,board):
        ''' This method helps us to implement the next move for this player against an opponent
        Parameters:
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        Returns:
        move- A tuple consisting of the x and y coordinates of the position where the player puts his coin
         '''
        valid_moves = self.get_all_valid_moves(board)     # generating a list of valid moves within the current board
        if not len(valid_moves):     # if there are no valid_moves
            return None
        move = self.alpha_beta(board, self.my_color, 5, self.min_value, self.max_value)  # if there is/are valid moves
        return move[0]

    def alpha_beta(self, board, player, depth, alpha, beta):
        ''' This method helps us implement minimax with alpha-beta prunning to determine the best move for the player
        Parameters:
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        player - integer or symbol which helps us identify the player or the opponent
        depth - The depth of the minimax tree developed for the player and opponent
        alpha - The constantly changing lower limit value of the minimax tree
        beta - The constantly changing upper limit value of the minimax tree
        Returns:
        move, val- Tuple consisting of the best move calculated from the characteristic heuristic function and the value
        '''
        moves = self.get_all_valid_moves(board)  #the list of possible next moves
        if depth == 0 or moves is None:    # if we are at the top of the tree or there are no more legal moves
            return (None, self.heuristics(board, player))
        best_move = moves[0]          # initialising the best move to be calculated from the heuristics
        if player == self.my_color:   # if we are considering the maximum value
            val = self.min_value     # initialising the maximum value
            for move in moves:        # iterating through the different possible moves to get the best one
                test_board = copy.deepcopy(board)        # copying the current board to get an idea of the possibility
                test_board = self.simulated_move(test_board, move)  # producing simulated board after a simulated move
                # game = GameBoard(self.board_size, self.my_color, self.opponent_color, -1)
                # game.board = board
                # test_board = game.board
                # game.play_move(list(move), player)
                # test_board = game.board
                v = self.alpha_beta(test_board, self.opponent_color, depth - 1, alpha, beta)[1]     # getting the simulated value from minimax using simulated board
                if v > val:          # if the simulated value is greater than the value we current
                    val = v          # replacing the new maximum with the old
                    best_move = move  # updating the value of the best move
                alpha = max(alpha, val)  # updating the value of alpha
                if beta <= alpha:         # breaking condition
                    break # beta cut-off
        else:                     # if we are considering the minimum value
            val = self.max_value           # initialising the minimum value 
            for move in moves:    # iterating through the different possible moves to get the best one
                test_board = copy.deepcopy(board)    # copying the current board to get an idea of the possibility
                test_board = self.simulated_move(test_board, move)   # producing simulated board after a simulated move
                # game = GameBoard(self.board_size, self.my_color, self.opponent_color, -1)
                # game.board = board
                # test_board = game.board
                # game.play_move(list(move), player)
                # test_board = game.board
                v = self.alpha_beta(test_board, self.my_color, depth - 1, alpha, beta)[1]        # getting the simulated value from minimax using simulated board
                if v < val:          # if the simulated value is greater than the value we current
                    val = v          # replacing the new maximum with the old
                    best_move = move # updating the value of the best move
                beta = min(beta, val) # updating the value of alpha
                if beta <= alpha:     # breaking condition
                    break # beta cut-off
        return best_move, val


    def heuristics(self, board, player):
        '''This method computes the defined heuristics which enables us to pick the best next move
        Parameters:
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        player - integer or symbol which helps us identify the player or the opponent
        Returns:
        num - An integer which represents the calculated heuristic function
        '''
        num = 0            # initialising the heuristic value of this move
        # iterating through all the positions in the board for proper calculation
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == player:    # if my player
                    if (i == 0 or i == self.board_size - 1) and (j == 0 or j == self.board_size - 1):
                        num += 4 # corner
                    elif (i == 0 or i == self.board_size - 1) or (j == 0 or j == self.board_size - 1):
                        num += 2 # side
                    else:
                        num += 1 # otherwise
                else:  # if my opponent
                    if (i == 0 or i == self.board_size - 1) and (j == 0 or j == self.board_size - 1):
                        num -= 4 # corner
                    elif (i == 0 or i == self.board_size - 1) or (j == 0 or j == self.board_size - 1):
                        num -= 2 # side
                    else:
                        num -= 1 # otherwise
        return num
    
    def simulated_move(self, board, move):
        ''' This method gives us the simulated board from a simulated move
        Parameters:
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        move - A tuple consisting of the x and y coordinates of a simulated move
        Returns:
        board- The simulated_board gotten from the simulated move
        '''
        # The possibilities of changes within the board for whivch the coins can be swapped
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        # The x and y coordinates of the simullated_move
        pos_x = move[0]
        pos_y = move[1]
        
        for i in range(8):
            # adding the first possible swap to the current coordinates
            row, col = dx[i], dy[i] 
            row += pos_x
            col += pos_y
            # initialising the list of turned stones in the game
            turned_stones = []
            # while the new coordinates are within the board
            while (row >= 0) and (row <= (self.board_size-1)) and (col >= 0) and (col <= (self.board_size-1)):
                if board[row][col] == self.opponent_color:   # if my opponent
                    turned_stones.append((row, col))
                elif board[row][col] == -1:       # if nothing
                    break
                else:                 # if my player
                    # turning my opponents stones to mine once it reaches my stone
                    for r, c in turned_stones:
                        board[r][c] = self.my_color
                #adding again for the second possible swap
                row += dx[i]
                col += dy[i]
        return board


    def __is_correct_move(self, move, board):
        '''This method actually confirms if the move is a legal move
        Parameters:
        move - A list consisting of both x and y coordinates of the proposed move
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        Returns:
        A boolean value which corresponds to if the move is possible(True) or if it is not (False)
        '''
        # A list of the possible coordinates with each index corresponding to possible swap directions
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        # iterating through each possible direction
        for i in range(len(dx)):
            if self.__confirm_direction(move, dx[i], dy[i], board)[0]:   # the condition on if we have swapped all possibilities
                return True
        return False

    def __confirm_direction(self, move, dx, dy, board):
        '''This method helps confirm that we have swapped in a particular direction
        Parmeters:
        move - A list consisting of both x and y coordinates of the proposed move
        dx - The x coordinate of the direction of swapping
        dy - The y coordinate of the direction of swapping
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        Returns:
        A tuple consisting of a boolean value which corresponds to the possible swapping or not and the number of swapped stones
        '''
        # adding the first possible swap to the current coordinates
        posx = move[0]+dx    
        posy = move[1]+dy
        opp_stones_inverted = 0    # initialising the number of swapped stones
        # the condition of the move being within the board
        if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
            if board[posx][posy] == self.opponent_color: # if it is my opponent
                opp_stones_inverted += 1
                # condition of the move being within the board
                while (posx >= 0) and (posx <= (self.board_size-1)) and (posy >= 0) and (posy <= (self.board_size-1)):
                    posx += dx      # adding the next possible swap to the current x coordinates
                    posy += dy      # adding the next possible swap to the current y coordinates
                    # condition of the new move being within the board
                    if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                        if board[posx][posy] == -1:   # if it is empty
                            return False, 0
                        if board[posx][posy] == self.my_color:   # if it is my player
                            return True, opp_stones_inverted
                    opp_stones_inverted += 1
        return False, 0

    def get_all_valid_moves(self, board):
        '''This method gets us all the possible valid moves.
        Parameters:
        board - A n x n matrix consisting of the positions taken up by the player and opponent
        Returns:
        valid_moves- A list consisting of tuples of coordinates of possible valid moves
        '''
        valid_moves = []    # initialising the list of possible valid moves
        # iterating through the positions in the board
        for x in range(self.board_size):
            for y in range(self.board_size):
                if (board[x][y] == -1) and self.__is_correct_move([x, y], board):   # if empty and is valid
                    valid_moves.append( (x, y) )

        if len(valid_moves) <= 0:   # if there are no more valid moves
            print('No possible move!')
            return None
        return valid_moves
    
