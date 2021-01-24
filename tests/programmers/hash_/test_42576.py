from typing import List

import pytest
from src.programmers.hash_.p42576 import solution


@pytest.mark.parametrize(
    "participant,completion,expect",
    [
        (["leo", "kiki", "eden"], ["eden", "kiki"], "leo"),
        (
            ["marina", "josipa", "nikola", "vinko", "filipa"],
            ["josipa", "filipa", "marina", "nikola"],
            "vinko",
        ),
        (
            ["mislav", "stanko", "mislav", "ana"],
            ["stanko", "ana", "mislav"],
            "mislav",
        ),
    ],
)
def test_solution(
    participant: List[str], completion: List[str], expect: str
) -> None:
    result = solution(participant=participant, completion=completion)
    assert result == expect
