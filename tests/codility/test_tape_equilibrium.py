from typing import List

import pytest
from src.codility.tape_equilibrium import solution


@pytest.mark.parametrize("A, expect", [([3, 1, 2, 4, 3], 1)])
def test_solution(A: List[int], expect: int) -> None:
    result = solution(A)
    assert result == expect
