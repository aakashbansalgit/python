from copy import deepcopy


#tic tac toe board
class Board():
    #constructor
    def __init__(self, board = None):
        #define players
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.empsqure = '_'
        
        #board position
        self.position = {}
        
        # reset board
        self.init_board()
        
        
        #copy of previous board state (if available)
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)
        
    #reset board
    def init_board(self):
        #loop over board rows
        for row in range (3):
            #loop over board columns
            for col in range (3):
                self.position[row,col] = self.empsqure
    
    
    
    def make_move(self, row, col):
        board = Board()
        board.position[row, col] = self.player_1
        (board.player_1,board.player_2) = (board.player_2,board.player_1)
        return board
    
    def is_draw(self):
        for row,col in self.position:
            if self.position[row,col] == self.empsqure:
                return False
        return True
    
    def is_win(self):
        for col in range(3):
            winning_sequence = []
            for row in range(3):
                if self.position[row,col] == self.player_2:
                    winning_sequence.append((row,col))
                if len(winning_sequence) == 3:
                    return True
                
        for row in range(3):
            winning_sequence = []
            for col in range(3):
                if self.position[row,col] == self.player_2:
                    winning_sequence.append((row,col))
                if len(winning_sequence) == 3:
                    return True
        
        winning_sequence = []
        for row in range(3):
            col = row
            if self.position[row,col] == self.player_2:
                winning_sequence.append((row,col))
            if len(winning_sequence) == 3:
                return True
        
        winning_sequence = []
        for row in range(3):
            col = 2 - row
            if self.position[row,col] == self.player_2:
                winning_sequence.append((row,col))
            if len(winning_sequence) == 3:
                return True
            
        return False
    
    def generate_states(self):
        #get list of valid moves
        actions = []
        
        for row in range (3):
            for col in range (3):
                if self.positon[row,col] == self.empsqure:
                    actions.append(self.make_move(row,col))
        #return list of valid actions (board instances)
        return actions
        
                 
    def __str__(self):
        #string representation of board
        board_string = ''
        #loop over row and columns
        for row in range (3):
            for col in range (3):
                board_string +=  ' %s' %self.position[row,col]
            board_string += '\n'
        board_string = '\n-------------\n' + self.player_1 + ' to move: \n-------------\n' + board_string
        
        #return
        return board_string





#main
if __name__ == '__main__':
    #board instance
    board = Board()
    print (board)
    board = board.make_move(2,1)
    print (board)
    if board.is_win():
        print (board.player_2 + "Won")
    elif board.is_draw():
        print("No Winner")
        
    
    board1 = Board(board)
    print (board1)
