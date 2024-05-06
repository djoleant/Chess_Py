# Imports
from Piece import *
from Piece import *
import os


# Constants
WHITE = 1
BLACK = 0
mapping123 = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
mappingABC = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

# Global variables
existingGame = None # Name of the file of the current game if opened from a file

# Functions

def save_board(board, file_path):
    # TODO: add SAVING the context like eaten pieces, check, checkmate, next player, etc.
    with open(file_path, 'w') as file:
        for row in board:
            line = ' '.join([str(piece) if piece is not None else '-' for piece in row])
            file.write(line + '\n')

def open_board(file_path):
    """
    Opens a file containing a chess board configuration and returns a 2D list representing the board.

    Args:
        file_path (str): The path to the file containing the chess board configuration.

    Returns:
        list: A 2D list representing the chess board. Each element in the list represents a square on the board.
              None represents an empty square, and instances of chess pieces represent occupied squares.

    Example:
        If the file at 'file_path' contains the following configuration:
        r n b q k b n r
        p p p p p p p p
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        - - - - - - - -
        P P P P P P P P
        R N B Q K B N R

        The function will return the following 2D list:
        [
            [Rock(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK), King(BLACK), Bishop(BLACK), Knight(BLACK), Rock(BLACK)],
            [Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)],
            [Rock(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE), King(WHITE), Bishop(WHITE), Knight(WHITE), Rock(WHITE)]
        ]
    """
    # TODO: add LOADING the context like eaten pieces, check, checkmate, next player, etc.
    board = []
    with open(file_path, 'r') as file:
        for line in file:
            row = []
            for piece in line.strip().split():
                if piece == '-':
                    row.append(None)
                else:
                    color = BLACK if piece.islower() else WHITE
                    symbol = piece.lower()
                    if symbol == 'r':
                        row.append(Rock(color))
                    elif symbol == 'n':
                        row.append(Knight(color))
                    elif symbol == 'b':
                        row.append(Bishop(color))
                    elif symbol == 'q':
                        row.append(Queen(color))
                    elif symbol == 'k':
                        row.append(King(color))
                    elif symbol == 'p':
                        row.append(Pawn(color))
            board.append(row)
    return board

def save_board_to_file(board):
    file_name = "saves/board_"
    number = 1
    while os.path.exists(file_name + str(number) + ".txt"):
        number += 1
    file_name += str(number) + ".txt"
    
    if existingGame is not None:
        choice = input("Do you want to update the current file? (y/n): ")
        if choice.lower() == 'y':
            file_name = existingGame
    
    save_board(board, "saves/" + file_name)


def open_board_from_file():
    file_name = input("Enter file name: ")
    if not os.path.exists("saves/" + file_name):
        print("File does not exist.")
        return None
    
    global existingGame
    existingGame = file_name
    
    return open_board("saves/" + file_name)