# Imports
from Piece import *
from Files import *
import os


# Constants
WHITE = 1
BLACK = 0
mapping123 = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
mappingABC = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


# Global variables
next = WHITE # Next player to move
check = False # Whether the current player is in check
checkmate = False # Whether the current player is in checkmate
eatenWHITE = []
eatenBLACK = []

EXITSIG = False # Exit signal

# Initialization

def initialize():
    board = [[None] * 8 for _ in range(8)]
    
    # Place white pieces
    board[7][0] = Rock(WHITE)
    board[7][1] = Knight(WHITE)
    board[7][2] = Bishop(WHITE)
    board[7][3] = Queen(WHITE)
    board[7][4] = King(WHITE)
    board[7][5] = Bishop(WHITE)
    board[7][6] = Knight(WHITE)
    board[7][7] = Rock(WHITE)
    for i in range(8):
        board[6][i] = Pawn(WHITE)
        
    # Place black pieces
    board[0][0] = Rock(BLACK)
    board[0][1] = Knight(BLACK)
    board[0][2] = Bishop(BLACK)
    board[0][3] = Queen(BLACK)
    board[0][4] = King(BLACK)
    board[0][5] = Bishop(BLACK)
    board[0][6] = Knight(BLACK)
    board[0][7] = Rock(BLACK)
    for i in range(8):
        board[1][i] = Pawn(BLACK)
    return board

def print_board(board):

    print("    a b c d e f g h")
    print("    ---------------")
    
    for i, row in enumerate(board):
        row = ["-" if element is None else element.symbol for element in row]
        print(f"{8-i} |"f" {' '.join(row)}")  # Print row number and elements
    print("")

def play_move(board):
    global check
    global checkmate
    while not checkmate or not EXITSIG:
        done = False
        while not done:
            global next
            
            start = input("Enter start position: ")
            if start == "exit":
                EXITSIG = True
                break
            
            start = start.split()
            start[0]=mapping123[start[0]]
            start[1]=mappingABC[start[1]]
            
            end = input("Enter end position: ")
            end = end.split()
            end[0]=mapping123[end[0]]
            end[1]=mappingABC[end[1]]
            
            piece = board[start[0]][start[1]]
            if piece is None:
                print("No piece at start position")
                done = False
            # elif piece.color != next: # TODO: temp commented for test purposes 
            #     print("Not your turn")
            #     done = False
            elif not piece.valid_direction(board, start, end):
                print("Invalid move")
                done = False
            else:
                _, capture = piece.valid_direction(board, start, end)
                print ("Capture: ", capture)
                if capture is not None:
                    eatenWHITE.append(board[capture[0]][capture[1]] if next else eatenBLACK.append(board[capture[0]][capture[1]]))
                    print("Eaten pieces: ", eatenWHITE if next else eatenBLACK) # TODO: eaten to be showed diff way
                board[end[0]][end[1]] = piece
                board[start[0]][start[1]] = None
                next = BLACK if next else WHITE
                print("Next is", "White" if next else "Black")
                done = True
            print_board(board)
        
        if start == "exit":
            break
            
    if EXITSIG:
        print("Do you want to save the game?")
        if input("y/n: ") == "y":
            save_board_to_file(board)
        
def force_move(board, start, end): # for testing purposes
    piece = board[start[0]][start[1]]
    board[end[0]][end[1]] = piece
    board[start[0]][start[1]] = None
    return True



        
# Main
if __name__ == "__main__":
    
    choice = input("Do you want to load the board from a file? (y/n): ")
    if choice == "y":
        board = open_board_from_file()
    else:
        board = initialize()
    
    print_board(board)
    
    # test_pawn(board) works with diff play_move func
    
    play_move(board)
    
    print_board(board)
    
    
