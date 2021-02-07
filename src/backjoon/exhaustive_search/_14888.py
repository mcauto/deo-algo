""" 연산자 끼워넣기
https://www.acmicpc.net/problem/14888
"""
from typing import List, Tuple

NUMBERS: List[int] = []
maximum, minimum = -1_000_000_000, 1_000_000_000


def calculate(
    number: int, index: int, add: int, sub: int, multi: int, div: int
) -> None:
    global NUMBERS, maximum, minimum
    if index == len(NUMBERS):
        maximum = max(number, maximum)
        minimum = min(number, minimum)
        return
    else:
        if add:
            result = number + NUMBERS[index]
            op_counts = (add - 1, sub, multi, div)
            calculate(result, index + 1, *op_counts)
        if sub:
            result = number - NUMBERS[index]
            op_counts = (add, sub - 1, multi, div)
            calculate(result, index + 1, *op_counts)
        if multi:
            result = number * NUMBERS[index]
            op_counts = (add, sub, multi - 1, div)
            calculate(result, index + 1, *op_counts)
        if div:
            result = int(number / NUMBERS[index])
            op_counts = (add, sub, multi, div - 1)
            calculate(result, index + 1, *op_counts)


def solution(
    numbers: List[int], op_counts: Tuple[int, int, int, int]
) -> Tuple[int, int]:
    global NUMBERS
    NUMBERS = numbers
    N = len(numbers)
    calculate(numbers[0], 1, *op_counts)
    return (maximum, minimum)


# if __name__ == "__main__":
#     N = int(input().strip())
#     NUMBERS = [int(value) for value in input().strip().split()]
#     add, sub, multi, div = [int(count) for count in input().strip().split()]
#     solution(numbers=NUMBERS, op_counts=(add, sub, multi, div))
#     print(maximum)
#     print(minimum)
