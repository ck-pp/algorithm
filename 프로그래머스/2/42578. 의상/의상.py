def solution(clothes):
    ans = 1
    dict = {row[1]:[] for row in clothes}
    for name, type in clothes:
        dict[type].append(name)
    for value in dict.values():
        ans *= (len(value)+1)
    return ans - 1