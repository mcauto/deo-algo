from typing import List

import pytest
from src.codility.frog_river_one import solution


@pytest.mark.parametrize("X,A,expect", [(5, [1, 3, 1, 4, 2, 3, 5, 4], 6)])
def test_solution(X: int, A: List[int], expect: int) -> None:
    result = solution(X, A)
    assert result == expect
