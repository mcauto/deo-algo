from typing import List

import pytest
from src.codility.odd_occurrences_in_array import solution


@pytest.mark.parametrize("A,expect", [([9, 3, 9, 3, 9, 7, 9], 7)])
def test_solution(A: List[int], expect: int) -> None:
    result = solution(A)
    assert result == expect
