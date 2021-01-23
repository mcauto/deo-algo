import pytest
from src.programmers.p237741 import solution


@pytest.mark.parametrize(
    "s,n,result", [("AB", 1, "BC"), ("z", 1, "a"), ("a B z", 4, "e F d")]
)
def test_solution(s: str, n: int, result: str) -> None:
    answer = solution(s, n)
    assert answer == result
