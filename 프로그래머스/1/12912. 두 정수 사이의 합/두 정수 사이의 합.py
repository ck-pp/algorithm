def solution(a, b):
    start, end = min(a, b), max(a, b)
    return sum([n for n in range(start, end + 1)])