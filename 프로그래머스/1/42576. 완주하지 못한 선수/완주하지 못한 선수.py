def solution(participant, completion):
    res = {name:0 for name in participant}
    for name in participant:
        res[name] += 1
    for comp_name in completion:
        res[comp_name] -= 1
    return [name for name in res if res[name] > 0][0]