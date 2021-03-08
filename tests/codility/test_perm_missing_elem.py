from typing import List

import pytest
from src.codility.perm_missing_elem import solution


@pytest.mark.parametrize("A, expect", [([2, 3, 1, 5], 4)])
def test_solution(A: List[int], expect: int) -> None:
    result = solution(A)
    assert result == expect
