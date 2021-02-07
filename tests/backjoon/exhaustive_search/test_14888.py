from typing import List, Tuple

import pytest
from src.backjoon.exhaustive_search._14888 import solution


@pytest.mark.parametrize(
    "numbers,op_table,expect",
    [
        ([5, 6], (0, 0, 1, 0), (30, 30)),
        ([3, 4, 5], (1, 0, 1, 0), (35, 17)),
        ([1, 2, 3, 4, 5, 6], (2, 1, 1, 1), (54, -24)),
    ],
)
def test_14888(
    numbers: List[int],
    op_table: Tuple[int, int, int, int],
    expect: Tuple[int, int],
) -> None:
    result = solution(numbers, op_table)
    assert result == expect
