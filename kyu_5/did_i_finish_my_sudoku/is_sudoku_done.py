#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from kyu_5.did_i_finish_my_sudoku.sudoku_by_row import assert_sudoku_by_row
from kyu_5.did_i_finish_my_sudoku.sudoku_by_column import assert_sudoku_by_column
from kyu_5.did_i_finish_my_sudoku.sudoku_by_regions import assert_sudoku_by_region


def done_or_not(board: list) -> str:
    """
    return 'Finished!'
    or
    return 'Try again!'
    :param board:
    :return:
    """
    if assert_sudoku_by_column(board) and assert_sudoku_by_row(board) and assert_sudoku_by_region(board):
        return 'Finished!'

    return 'Try again!'
