from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Set


class PositionX(Enum):
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()


class PositionY(Enum):
    TOP = auto()
    MIDDLE = auto()
    BOTTOM = auto()


@dataclass
class Cell:
    value: Optional[int] = None
    is_original: bool = False


@dataclass
class SudokuBoard:
    board: List[List[Cell]]

    def is_solution_valid(self) -> bool:
        for row in self.board:
            if not self.is_group_valid(row):
                return False

        for col in range(9):
            column = self.get_column(col)
            if not self.is_group_valid(column):
                return False

        for position_y in PositionY:
            for position_x in PositionX:
                box = self.get_box(position_y, position_x)
                if not self.is_group_valid(box):
                    return False

        return all(cell.value is not None for row in self.board for cell in row)

    def is_group_valid(self, group: List[Cell]) -> bool:
        seen_values: Set[int] = set()

        for cell in group:
            if cell.value is not None and cell.value in seen_values:
                return False
            seen_values.add(cell.value)  # type: ignore

        return True

    def get_column(self, col: int) -> List[Cell]:
        return [self.board[row][col] for row in range(9)]

    def get_row(self, row: int) -> List[Cell]:
        return self.board[row]

    def get_box(self, position_y: PositionY, position_x: PositionX):
        start_row = (position_y.value - 1) * 3
        start_col = (position_x.value - 1) * 3

        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[start_row + i][start_col + j])
        return box
