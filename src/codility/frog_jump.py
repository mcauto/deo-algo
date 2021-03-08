import math


def solution(X: int, Y: int, D: int) -> int:
    result = (Y - X) / D
    return math.ceil(result)
