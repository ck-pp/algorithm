def solution(a, b):
    return sum(n1 * n2 for n1, n2 in zip(a, b))