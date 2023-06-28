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


def to_position_x(position: int) -> PositionX:
    match position:
        case 0 | 1 | 2:
            return PositionX.LEFT
        case 3 | 4 | 5:
            return PositionX.MIDDLE
        case 6 | 7 | 8:
            return PositionX.RIGHT
        case _:
            raise ValueError(f"Value {position} was not allowed, must be 0-8")

def to_position_y(position: int) -> PositionY:
    match position:
        case 0 | 1 | 2:
            return PositionY.TOP
        case 3 | 4 | 5:
            return PositionY.MIDDLE
        case 6 | 7 | 8:
            return PositionY.BOTTOM
        case _:
            raise ValueError(f"Value {position} was not allowed, must be 0-8")


@dataclass
class Cell:
    value: Optional[int] = None
    is_original: bool = False


@dataclass
class SudokuBoard:
    board: List[List[Cell]]

    @property
    def rows(self):
        return self.board

    @property
    def columns(self):
        num_columns = len(self.board[0])
        return [
            [self.board[row_idx][col_idx] for row_idx in range(len(self.board))]
            for col_idx in range(num_columns)
        ]

    def is_solution_valid(self) -> bool:
        for row in self.rows:
            if not self.is_group_valid(row):
                return False

        for column in self.columns:
            if not self.is_group_valid(column):
                return False

        for position_y in PositionY:
            for position_x in PositionX:
                box = self.get_box(position_y, position_x)
                if not self.is_group_valid(box):
                    return False

        return all(cell.value is not None for row in self.board for cell in row)

    def is_group_valid(self, group: List[Cell]) -> bool:
        if len(group) != 9:
            return False

        seen_values: Set[int] = set()

        for cell in group:
            if cell.value is None or cell.value < 1 or cell.value > 9:
                return False
            if cell.value in seen_values:
                return False
            seen_values.add(cell.value)

        return True

    def get_box(self, position_y: PositionY, position_x: PositionX):
        start_row = (position_y.value - 1) * 3
        start_col = (position_x.value - 1) * 3

        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[start_row + i][start_col + j])
        return box
