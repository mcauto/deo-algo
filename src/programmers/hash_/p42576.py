""" 완주하지 못한 선수
수많은 마라톤 선수들이 마라톤에 참여하였습니다.

단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와

완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,

완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""

from typing import List


def solution(participant: List[str], completion: List[str]) -> str:
    assert len(participant) <= 100_000
    assert len(completion) + 1 == len(participant)
    for person in participant:
        assert person.islower() and len(person) >= 1 and len(person) <= 20

    retired = {}
    for name in participant:
        if name not in retired:
            retired.update({name: 1})
        else:
            retired[name] += 1

    for name in completion:
        if retired[name] > 1:
            retired[name] -= 1
        else:
            del retired[name]

    return list(retired)[0]
