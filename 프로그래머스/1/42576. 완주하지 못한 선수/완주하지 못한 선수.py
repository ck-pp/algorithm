from collections import Counter

def solution(participant, completion):
    # 참여자 명단 - 이름: (동명이인) 수
    participant_num = Counter(participant)
    
    for c in completion:
        # 완주한 선수 빼기
        participant_num[c] -= 1
    
    # 남은 사람 == 완주하지 못한 선수
    return [name for name, num in participant_num.items() if num > 0][0]
        