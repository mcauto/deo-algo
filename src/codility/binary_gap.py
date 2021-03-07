def solution(N: int) -> int:
    gaps = [0]
    binary = bin(N)[2:]
    temp = int(binary[0])  # 첫번째 숫자 저장
    count = 0
    flag = False
    for value in binary[1:]:
        if temp ^ int(value):  # 숫자가 바뀐경우 카운트 시작
            flag = not flag
            temp = int(value)
        if flag:
            count += 1
        else:
            gaps.append(count)
            count = 0
    return max(gaps)
