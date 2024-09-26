def solution(s1, s2):
    return sum([1 if s1.count(s) + s2.count(s) > 1 else 0 for s in set(s1+s2)])