def solution(picture, k):
    ans = []
    for p in picture:
        p = p.replace('.', '.' * k).replace('x', 'x' * k)
        for _ in range(k):
            ans.append(p)
    return ans