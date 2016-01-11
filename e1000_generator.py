#!/usr/bin/env python
"""Generate random initial chess positions.

The white and black positions can be asymmetric;
thus, there are overall 960 * 960 = 921600 valid initial positions.
In hex, it is e1000.
"""

from __future__ import print_function

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


def initial_position_to_text(init_setup):
    """Prints initial setup positions into a text.

    Args:
        init_setup: A map of white and black non-pawn piece positions.

    Returns:
        A text representation of the position with pawns.
    """
    # NOTE: Unicode colors seem to be reversed in Python for chess pieces.
    whites = {
        "bishop_dark": u"\u2657",
        "bishop_white": u"\u2657",
        "knight_one": u"\u2658",
        "knight_two": u"\u2658",
        "queen": u"\u2655",
        "rook_one": u"\u2656",
        "rook_two": u"\u2656",
        "king": u"\u2654",
        }
    white_pawn = u"\u2659"

    blacks = {
        "bishop_dark": u"\u265D",
        "bishop_white": u"\u265D",
        "knight_one": u"\u265E",
        "knight_two": u"\u265E",
        "queen": u"\u265B",
        "rook_one": u"\u265C",
        "rook_two": u"\u265C",
        "king": u"\u265A",
        }
    black_pawn = u"\u265F"

    def order_setup(piece_positions):
        """Handles piece position transformations to a list.

        Returns:
            An ordered list of pieces.
        """
        order = ["a", "b", "c", "d", "e", "f", "g", "h"]
        ret = []
        for i in order:
            for k, v in piece_positions.items():
                if v == i:
                    ret.append(k)
                    break
        return ret

    text = ["8 " +
            " ".join([whites[x] for x in order_setup(init_setup["black"])]),
            "7" + 8 * u" \u2659"]
    text += [str(i) + " . . . . . . . ." for i in reversed(range(3, 7))]
    text += ["2" + 8 * u" \u265F",
             "1 " +
             " ".join([blacks[x] for x in order_setup(init_setup["white"])]),
             "  a b c d e f g h"]
    return "\n".join(text)

if __name__ == "__main__":
    print(initial_position_to_text(chess_e1000()))
