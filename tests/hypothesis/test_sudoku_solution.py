from datetime import timedelta

from hypothesis import Verbosity, given, settings
from hypothesis import strategies as st

from solver.board import Cell, SudokuBoard, to_position_x, to_position_y

from .strategies import integers_with_exclude


@given(st.data())
@settings(max_examples=20000, verbosity=Verbosity.normal, deadline=None)
def test_is_solution_invalid(data):
    sudoku = SudokuBoard(board=[
        [Cell(9), Cell(), Cell(), Cell(), Cell(2), Cell(), Cell(), Cell(8), Cell(1)],
        [Cell(2), Cell(), Cell(), Cell(), Cell(), Cell(9), Cell(4), Cell(), Cell()],
        [Cell(), Cell(7), Cell(), Cell(3), Cell(), Cell(5), Cell(), Cell(), Cell()],
        [Cell(), Cell(2), Cell(5), Cell(), Cell(), Cell(), Cell(8), Cell(), Cell()],
        [Cell(3), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(5)],
        [Cell(), Cell(), Cell(9), Cell(), Cell(), Cell(), Cell(1), Cell(3), Cell()],
        [Cell(), Cell(), Cell(), Cell(6), Cell(), Cell(7), Cell(), Cell(9), Cell()],
        [Cell(), Cell(), Cell(7), Cell(8), Cell(), Cell(), Cell(), Cell(), Cell(2)],
        [Cell(5), Cell(8), Cell(), Cell(), Cell(9), Cell(), Cell(), Cell(), Cell(4)],
    ])

    for row_index, row in enumerate(sudoku.rows):
        for column_index, cell in enumerate(row):
            if cell.value is None:
                row_values = {cell.value for cell in row if cell.value is not None}

                column = sudoku.columns[column_index]
                column_values = {cell.value for cell in column if cell.value is not None}

                position_x = to_position_x(column_index)
                position_y = to_position_y(row_index)
                box = sudoku.get_box(position_x=position_x, position_y=position_y)
                box_values = {cell.value for cell in box if cell.value is not None}

                impossible_values = row_values | column_values | box_values
                if len(impossible_values) == 9:
                    # this solution is wrong. might as well restart with another attempt
                    return

                cell.value = data.draw(integers_with_exclude(min_value=1, max_value=9, exclude=impossible_values))

    # Verify if the board is a valid solution
    assert not sudoku.is_solution_valid(), f"Solution of puzzle: {sudoku}"
