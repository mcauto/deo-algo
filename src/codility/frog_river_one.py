from typing import List


def solution(X: int, A: List[int]) -> int:
    S = set([])
    for seconds, num in enumerate(A):
        S.add(num)
        if len(S) == X:
            return seconds
    return -1
