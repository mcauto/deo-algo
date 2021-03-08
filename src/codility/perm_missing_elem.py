from typing import List


def solution(A: List[int]) -> int:
    n = len(A) + 1
    result = int((n * (n + 1)) / 2) - sum(A)
    return result
