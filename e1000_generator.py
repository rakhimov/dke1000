#!/usr/bin/env python
"""e1000_generator.py

Code for generation random initial chess positions. The white and black
positions can be asymmetric; thus, there are overall 960 * 960 = 921600
valid initial positions. In hex, it is e1000.
"""

from pprint import pprint
from random import randint, sample

def chess_960(color="white"):
    """Generates starting positions according to the rules of Chess960.

    Args:
        color: The color of pieces as the reference for positioning.

    Returns:
        Dictionary with piece names and their positions.
    """
    assert color == "white" or color == "black"
    pieces = {
            "bishop_dark": "",
            "bishop_white": "",
            "knight_one": "",
            "knight_two": "",
            "queen": "",
            "rook_one": "",
            "rook_two": "",
            "king": ""
            }
    empty_squares = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Determine positions of bishops. These are the only pieces picky about the
    # square colors. There are (4 choose 1) * (4 choose 1) = 16 possibilities.
    shift = 0 if color == "white" else 1  # adjustment for the reference side
    choice = randint(0, 3)
    pieces["bishop_dark"] = empty_squares[choice * 2 + shift]
    choice = randint(0, 3)
    pieces["bishop_white"] = empty_squares[choice * 2 + 1 - shift]

    empty_squares.remove(pieces["bishop_dark"])
    empty_squares.remove(pieces["bishop_white"])

    # Determine a position of a queen: (6 choose 1) = 6 possiblities.
    pieces["queen"] = sample(empty_squares, 1)[0]
    empty_squares.remove(pieces["queen"])

    # Determine positions of knights: (5 choose 2) = 10 possibilities.
    pos = sample(empty_squares, 2)
    pieces["knight_one"] = pos[0]
    pieces["knight_two"] = pos[1]
    empty_squares.remove(pieces["knight_one"])
    empty_squares.remove(pieces["knight_two"])

    # Determine positions of rooks and a king. There is only one choise left.
    assert len(empty_squares) == 3
    pieces["rook_one"] = empty_squares[0]
    pieces["king"] = empty_squares[1]
    pieces["rook_two"] = empty_squares[2]

    return pieces

def chess_e1000():
    """Generates asymmetric Chess960 initial positions.

    Returns:
        Dictionary of piece colors and their initial positions.
    """
    return {"white": chess_960("white"), "black": chess_960("black")}

if __name__ == "__main__":
    pprint(chess_e1000())
