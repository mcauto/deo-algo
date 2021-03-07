import pytest
from src.codility.binary_gap import solution


@pytest.mark.parametrize(
    "number,expect", [(9, 2), (529, 4), (32, 0), (1041, 5)]
)
def test_binary_gap(number: int, expect: int) -> None:
    result = solution(number)
    assert result == expect
