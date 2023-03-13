import copy
class MyPlayer():
    '''Template Docstring for MyPlayer, look at the TODOs''' # TODO a short description of your player

    def __init__(self, my_color,opponent_color, board_size):
        self.name = 'olasoolu' #TODO: fill in your username
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.board_size = board_size
        self.min_value = 0
        self.max_value = 1176

    def move(self,board):
        valid_moves = self.get_all_valid_moves(board)
        if not len(valid_moves):
            return None
        move = self.alpha_beta(board, self.my_color, 4, self.min_value, self.max_value)
        return move[0]

    def alpha_beta(self, board, player, depth, alpha, beta):
        moves = self.get_all_valid_moves(board)
        if depth == 0 or moves is None:
            return (None, self.heuristics(board, player))
        best_move = moves[0]
        if player == self.my_color:
            val = self.min_value
            for move in moves:
                test_board = copy.deepcopy(board)
                test_board = self.simulated_move(test_board, move)
                v = self.alpha_beta(test_board, self.opponent_color, depth - 1, alpha, beta)[1]
                if v > val:
                    val = v
                    best_move = move
                alpha = max(alpha, val)
                if beta <= alpha:
                    break # beta cut-off
        else:
            val = self.max_value
            for move in moves:
                test_board = copy.deepcopy(board)
                test_board = self.simulated_move(test_board, move)
                v = self.alpha_beta(test_board, self.my_color, depth - 1, alpha, beta)[1]
                if v < val:
                    val = v
                    best_move = move
                beta = min(beta, val)
                if beta <= alpha:
                    break # beta cut-off
        return best_move, v


    def heuristics(self, board, player):
        if self.board_size==6:
            MATRIX = [[120, -20,  20,  20, -20, 120],
                       [-20, -40,  -5,  -5, -40, -20],
                       [20,  -5,  15,  15,  -5,  20],
                       [20,  -5,  15,  15,  -5,  20],
                       [-20, -40,  -5,  -5, -40, -20],
                       [120, -20,  20,  20, -20, 120],
                       ]
        if self.board_size ==8:
            MATRIX = [[120, -20,  20,   5,   5,  20, -20, 120],
                       [-20, -40,  -5,  -5,  -5,  -5, -40, -20],
                       [20,  -5,  15,   3,   3,  15,  -5,  20],
                       [ 5,  -5,   3,   3,   3,   3,  -5,   5],
                       [5,  -5,   3,   3,   3,   3,  -5,   5],
                       [20,  -5,  15,   3,   3,  15,  -5,  20],
                       [-20, -40,  -5,  -5,  -5,  -5, -40, -20],
                       [120, -20,  20,   5,   5,  20, -20, 120],
                       ]
        if self.board_size == 10:
            MATRIX = [[120, -20,  20,   5,   5,   5,   5, 20, -20, 120],
                       [-20, -40,  -5,  -5,  -5,  -5,  -5,  -5, -40, -20],
                       [20,  -5,  15,   3,   3,   3,   3,  15,  -5,  20],
                       [ 5,  -5,   3,   3,   3,   3,   3,   3,  -5,   5],
                       [5,  -5,   3,   3,   3,   3,   3,   3,  -5,   5],
                       [ 5,  -5,   3,   3,   3,   3,   3,   3,  -5,   5],
                       [5,  -5,   3,   3,   3,   3,   3,   3,  -5,   5],
                       [20,  -5,  15,   3,   3,   3,   3,  15,  -5,  20],
                       [-20, -40,  -5,  -5,  -5,  -5,  -5,  -5, -40, -20],
                       [120, -20,  20,   5,   5,   5,   5,  20, -20, 120],
                       ]
                    
        num = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == player:
                    num += MATRIX[i][j]
                else:
                    num -= MATRIX[i][j]
        return num
    
    def simulated_move(self, board, move):
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        pos_x = move[0]
        pos_y = move[1]
        
        for i in range(8):
            row, col = dx[i], dy[i]
            row += pos_x
            col += pos_y
            turned_stones = []
            while (row >= 0) and (row <= (self.board_size-1)) and (col >= 0) and (col <= (self.board_size-1)):
                if board[row][col] == self.opponent_color:
                    turned_stones.append((row, col))
                elif board[row][col] == -1:
                    break
                else:
                    for r, c in turned_stones:
                        board[r][c] = self.my_color
                row += dx[i]
                col += dy[i]
        return board


    def __is_correct_move(self, move, board):
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(len(dx)):
            if self.__confirm_direction(move, dx[i], dy[i], board)[0]:
                return True
        return False

    def __confirm_direction(self, move, dx, dy, board):
        posx = move[0]+dx
        posy = move[1]+dy
        opp_stones_inverted = 0
        if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
            if board[posx][posy] == self.opponent_color:
                opp_stones_inverted += 1
                while (posx >= 0) and (posx <= (self.board_size-1)) and (posy >= 0) and (posy <= (self.board_size-1)):
                    posx += dx
                    posy += dy
                    if (posx >= 0) and (posx < self.board_size) and (posy >= 0) and (posy < self.board_size):
                        if board[posx][posy] == -1:
                            return False, 0
                        if board[posx][posy] == self.my_color:
                            return True, opp_stones_inverted
                    opp_stones_inverted += 1
        return False, 0

    def get_all_valid_moves(self, board):
        valid_moves = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                if (board[x][y] == -1) and self.__is_correct_move([x, y], board):
                    valid_moves.append( (x, y) )

        if len(valid_moves) <= 0:
            print('No possible move!')
            return None
        return valid_moves
    
