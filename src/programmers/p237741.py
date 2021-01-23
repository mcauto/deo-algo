"""
시저암호
AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
z는 1만큼 밀면 a가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만들기
"""


def solution(s: str, n: int) -> str:
    assert n in range(0, 26)
    assert len(s) <= 8000
    answer = ""
    for ch in s:
        if ch == " ":
            answer += " "
        elif ch.isupper():
            answer += chr((ord(ch) - ord("A") + n) % 26 + ord("A"))
        elif ch.islower():
            answer += chr((ord(ch) - ord("a") + n) % 26 + ord("a"))

    return answer
