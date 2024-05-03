# Imports

# Constants
WHITE = 1
BLACK = 0

# Global variables

# Classes
class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = None
        self.name = None
        
    def __str__(self):
        return self.symbol
    
    # TODO: out of board check ¡¡¡FOR EVERY PIECE!!!
    def valid_direction(self, board, start, end):
        raise NotImplementedError("Subclasses must implement this method")
    
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "P" if color == WHITE else "p"
        self.name = "Pawn"
        
    # TODO: add that it can't go more than 2 if not first movement
    # TODO: check if no piece in between if it's a 2 step movement
    def valid_direction(self, board, start, end):
        if self.color == WHITE:
            if start[0] - end[0] == 2 and start[0] == 6:
                return (True, None)
            elif (start[0] - end[0] == 1 or start[0] - end[0] == 1) and abs(end[1] - start[1]) == 0 and board[end[0]][end[1]] is None:
                return (True, None)
            elif start[0] - end[0] == 1 and abs(end[1] - start[1]) == 1 and board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == BLACK:
                return (True, [end[0], end[1]])
            return False
        else:
            if end[0] - start[0] == 2 and start[0] == 1:   
                return (True, None)
            elif (end[0] - start[0] == 1 or end[0] - start[0] == 2) and abs(end[1] - start[1]) == 0 and board[end[0]][end[1]] is None:
                return (True, None)
            elif end[0] - start[0] == 1 and abs(end[1] - start[1]) == 1 and board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == WHITE:
                return (True, [end[0], end[1]])
            return False
        
class Rock(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "R" if color == WHITE else "r"
        self.name = "Rock"
    
    def check_between(self, board, start, end):
        if start[0] == end[0] and start[1] != end[1]:
            # Check if there are any pieces in between
            for i in range(start[1]+1, end[1]):
                if board[start[0]][i] is not None:
                    print("Something in between 1")
                    return (False, None)
        elif start[1] == end[1] and start[0] != end[0]:
            # Check if there are any pieces in between
            for i in range(start[0]+1, end[0]):
                if board[i][start[1]] is not None:
                    print("Something in between 2")
                    return (False, None)
        
        return (True, None)
            
    
    # def valid_direction(self, board, start, end):
    #     if board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == self.color:
    #         return (False, None)
    
    def valid_direction(self, board, start, end):
        if board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == self.color:
            print("check 0 failed")
            return False
        
        if start[0] == end[0] and start[1] != end[1]:
            # Determine the direction of the loop
            if start[1] < end[1]:
                for j in range(start[1] + 1, end[1]):
                    if board[start[0]][j] is not None:
                        print("check 1 failed")
                        return False
            else:
                for j in range(start[1] - 1, end[1], -1):
                    if board[start[0]][j] is not None:
                        print("check 1 failed")
                        return False
            
            if board[end[0]][end[1]] is None:
                print("check 2 OK")
                return (True, None)
            # Check if the end position has a piece of the opposite color
            elif board[end[0]][end[1]].color != self.color:
                print("check 3 OK")
                return (True, [end[0], end[1]])
            
            print("check 4 failed")
            return False
        
        elif start[1] == end[1] and start[0] != end[0]:
            # Check if there are any pieces in between
            # Determine the direction of the loop
            if start[0] < end[0]:
                # Forward loop (start[0] < end[0])
                for i in range(start[0] + 1, end[0]):
                    if board[i][start[1]] is not None:
                        return False
            else:
                # Backward loop (start[0] > end[0])
                for i in range(start[0] - 1, end[0], -1):
                    if board[i][start[1]] is not None:
                        return False
                    
            if board[end[0]][end[1]] is None:
                print("check 6 OK")
                return (True, None)
            # Check if the end position has a piece of the opposite color
            elif board[end[0]][end[1]].color != self.color:
                print("check 7 OK")
                return (True, [end[0], end[1]])
            
            print("check 8 failed")
            return False
        
        print("check 9 failed")
        return False
            
        
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "N" if color == WHITE else "n"
        self.name = "Knight"
    
    def valid_direction(self, board, start, end):
        if board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == self.color:
            return False
        
        if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
            if board[end[0]][end[1]] is None:
                return (True, None)
            elif board[end[0]][end[1]].color != self.color:
                return (True, [end[0], end[1]])
            
        elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
            if board[end[0]][end[1]] is None:
                return (True, None)
            elif board[end[0]][end[1]].color != self.color:
                return (True, [end[0], end[1]])

        return False
        
    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "B" if color == WHITE else "b"
        self.name = "Bishop"
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "Q" if color == WHITE else "q"
        self.name = "Queen"
        
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "K" if color == WHITE else "k"
        self.name = "King"
        