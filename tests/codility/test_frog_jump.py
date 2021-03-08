import pytest
from src.codility.frog_jump import solution


@pytest.mark.parametrize("X,Y,D,expect", [(10, 85, 30, 3)])
def test_solution(X: int, Y: int, D: int, expect: int) -> None:
    result = solution(X, Y, D)
    assert result == expect
