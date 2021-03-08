from typing import List


def solution(A: List[int]) -> int:
    result: int
    left_tape = 0
    right_tape = sum(A)  # 미리 오른쪽 테이프합을 구해둠 O(n)
    for P in range(1, len(A)):  # O(n)
        left_tape += A[P - 1]  # 왼쪽 테이프 값을 하나씩 더함
        right_tape -= A[P - 1]  # 오른쪽 테이프 값을 하나씩 뺌
        difference = abs(left_tape - right_tape)  # 양 테이프 차이 구하기
        if P != 1:
            result = min(result, difference)
        else:
            result = difference
    return result
