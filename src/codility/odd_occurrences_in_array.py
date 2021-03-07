from typing import Dict, List


def solution(A: List[int]) -> int:
    # 짝이 없는 정수 반환하기
    result = 0
    for num in A:
        result ^= num
    return result
