from typing import List


def solution(A: List[int], K: int) -> List[int]:
    # K만큼 우측으로 회전 시키기
    result = [0 for _ in range(len(A))]
    for index, num in enumerate(A):
        position = (index + K) % len(A)
        result[position] = num
    return result
