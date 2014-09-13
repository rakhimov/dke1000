#! usr/bin/env python

from random import randint, sample

def chess_960():
    """Generates starting positions according to the rules of Chess960
    Returns:
        A dictionary with piece names and their positions.
    """
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
    black_squares = ["a", "c", "e", "g"]
    white_squares = ["b", "d", "f", "h"]
    empty_squares = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Determine positions of bishops.
    choice = randint(0, 3)
    pieces["bishop_dark"] = black_squares[choice]
    empty_squares.remove(pieces["bishop_dark"])
    choice = randint(0, 3)
    pieces["bishop_white"] = white_squares[choice]
    empty_squares.remove(pieces["bishop_white"])

    # Determine a position of a queen.
    pieces["queen"] = sample(empty_squares, 1)[0]
    empty_squares.remove(pieces["queen"])

    # Determine positions of knights.
    pos = sample(empty_squares, 2)
    pieces["knight_one"] = pos[0]
    pieces["knight_two"] = pos[1]
    empty_squares.remove(pieces["knight_one"])
    empty_squares.remove(pieces["knight_two"])

    # Determine positions of rooks and a king.
    assert(len(empty_squares) == 3)
    pieces["rook_one"] = empty_squares[0]
    pieces["king"] = empty_squares[1]
    pieces["rook_two"] = empty_squares[2]

    return pieces

if __name__ == "__main__":
    print("White pieces:")
    print(chess_960())
    print("\nBlack pieces:")
    print(chess_960())
