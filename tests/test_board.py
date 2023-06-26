from solver.board import Cell, SudokuBoard

# Positive and negative test cases for is_group_valid method
positive_group = [Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9)]
negative_group = [Cell(1), Cell(2), Cell(2), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9)]

# Positive and negative test cases for is_solution_valid method
positive_solution = [
    [
        Cell(5, True),
        Cell(3, True),
        Cell(4),
        Cell(6),
        Cell(7, True),
        Cell(8),
        Cell(9),
        Cell(1),
        Cell(2),
    ],
    [
        Cell(6, True),
        Cell(7),
        Cell(2),
        Cell(1, True),
        Cell(9, True),
        Cell(5, True),
        Cell(3),
        Cell(4),
        Cell(8),
    ],
    [
        Cell(1),
        Cell(9, True),
        Cell(8, True),
        Cell(3),
        Cell(4),
        Cell(2),
        Cell(5),
        Cell(6, True),
        Cell(7),
    ],
    [
        Cell(8, True),
        Cell(5),
        Cell(9),
        Cell(7),
        Cell(6, True),
        Cell(1),
        Cell(4),
        Cell(2),
        Cell(3, True),
    ],
    [
        Cell(4, True),
        Cell(2),
        Cell(6),
        Cell(8, True),
        Cell(5),
        Cell(3, True),
        Cell(7),
        Cell(9),
        Cell(1, True),
    ],
    [
        Cell(7, True),
        Cell(1),
        Cell(3),
        Cell(9),
        Cell(2, True),
        Cell(4),
        Cell(8),
        Cell(5),
        Cell(6, True),
    ],
    [
        Cell(9),
        Cell(6, True),
        Cell(1),
        Cell(5),
        Cell(3),
        Cell(7),
        Cell(2, True),
        Cell(8, True),
        Cell(4),
    ],
    [
        Cell(2),
        Cell(8),
        Cell(7),
        Cell(4, True),
        Cell(1, True),
        Cell(9, True),
        Cell(6),
        Cell(3),
        Cell(5, True),
    ],
    [
        Cell(3),
        Cell(4),
        Cell(5),
        Cell(2),
        Cell(8),
        Cell(6),
        Cell(1),
        Cell(7, True),
        Cell(9, True),
    ],
]

negative_solution = [
    [
        Cell(5, True),
        Cell(3, True),
        Cell(4),
        Cell(6),
        Cell(7, True),
        Cell(8),
        Cell(9),
        Cell(1),
        Cell(2),
    ],
    [
        Cell(6, True),
        Cell(7),
        Cell(2),
        Cell(1, True),
        Cell(9, True),
        Cell(5, True),
        Cell(3),
        Cell(4),
        Cell(8),
    ],
    [
        Cell(1),
        Cell(9, True),
        Cell(8, True),
        Cell(3),
        Cell(4),
        Cell(2),
        Cell(5),
        Cell(6, True),
        Cell(7),
    ],
    [
        Cell(8, True),
        Cell(5),
        Cell(9),
        Cell(7),
        Cell(6, True),
        Cell(1),
        Cell(4),
        Cell(2),
        Cell(3, True),
    ],
    [
        Cell(4, True),
        Cell(2),
        Cell(6),
        Cell(8, True),
        Cell(5),
        Cell(3, True),
        Cell(7),
        Cell(9),
        Cell(1, True),
    ],
    [
        Cell(7, True),
        Cell(1),
        Cell(3),
        Cell(9),
        Cell(2, True),
        Cell(4),
        Cell(8),
        Cell(5),
        Cell(6, True),
    ],
    [
        Cell(9),
        Cell(6, True),
        Cell(1),
        Cell(5),
        Cell(3),
        Cell(7),
        Cell(2, True),
        Cell(8, True),
        Cell(4),
    ],
    [
        Cell(2),
        Cell(8),
        Cell(7),
        Cell(4, True),
        Cell(1, True),
        Cell(9, True),
        Cell(6),
        Cell(3),
        Cell(5, True),
    ],
    [
        Cell(3),
        Cell(4),
        Cell(5),
        Cell(2),
        Cell(8),
        Cell(6),
        Cell(1),
        Cell(7, True),
        Cell(8, True),
    ],  # Invalid value here
]

empty_solution = [[Cell() for _ in range(9)] for _ in range(9)]

# Create the SudokuBoard instance for testing
sudoku = SudokuBoard(board=[])


# Define the unit tests using pytest
def test_is_group_valid_positive():
    assert sudoku.is_group_valid(positive_group) is True


def test_is_group_valid_negative():
    assert sudoku.is_group_valid(negative_group) is False


def test_is_solution_valid_positive():
    sudoku.board = positive_solution
    assert sudoku.is_solution_valid() is True


def test_is_solution_valid_negative():
    sudoku.board = negative_solution
    assert sudoku.is_solution_valid() is False


def test_is_solution_valid_empty():
    sudoku.board = empty_solution
    assert sudoku.is_solution_valid() is False


def test_is_group_valid_invalid_value():
    invalid_group = [
        Cell(5), Cell(3), Cell(0),  # Invalid value here
        Cell(6), Cell(7), Cell(1),
        Cell(2), Cell(9), Cell(8)
    ]

    assert sudoku.is_group_valid(invalid_group) == False
