def solution(picture, k):
    ans = []
    for p in picture:
        for _ in range(k):
            ans.append(p.replace('.', '.' * k).replace('x', 'x' * k))
    return ans