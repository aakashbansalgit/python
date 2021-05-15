from copy import deepcopy
import sys


#tic tac toe board
class Board():
    #constructor
    def __init__(self, board = None):
        #define players
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.empsqure = '-'
        
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
        board = Board(self)
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
                if self.position[row,col] == self.empsqure:
                    
                    actions.append(self.make_move(row,col))
        #return list of valid actions (board instances)
        return actions
    
    def game_loop(self):
        print ("\n Tic Tac Toe - Reiforced Learning\n")
        print ('Enter the move!\nFormat: 1,1 (as in [x][y] where x is column and y is row)\nType exit to quit the game')
        print (self)
        while True:
            user_input = input('>')
            if user_input == 'exit':
                sys.exit()
            if user_input == '':
                continue
            try:
                row = int(user_input.split(',')[1]) -1
                col = int(user_input.split(',')[0]) -1
                if self.position[row,col] !=self.empsqure:
                    print ('Illegal Move!')
                    continue
                self = self.make_move(row,col)
                
                print (self)
                if self.is_win():
                    print (self.player_2, "WON the Game!")
                    break
                elif self.is_draw():
                    print ("Game is Drawn!")
                    break
                
                    
            except Exception as e:
                print('Error:', e)
                print ('Illegal Command!')
                print ('Move Format: 1,1 (as in [x][y] where x is column and y is row)')
                 
                 
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
    board.game_loop()
