from typing import List

import pytest
from src.codility.cyclic_rotation import solution


@pytest.mark.parametrize(
    "A,K,expect",
    [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([0, 0, 0], 1, [0, 0, 0]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ],
)
def test_solution(A: List[int], K: int, expect: List[int]) -> None:
    result = solution(A, K)
    assert result == expect
