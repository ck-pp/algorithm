from collections import deque

def solution(topping):
    ans = 0
    cake1 = set()
    cake2 = {idx:0 for idx in set(topping)}
    for j in topping:
        cake2[j] += 1
    for i in topping:
        cake1.add(i)
        cake2[i] -= 1
        if cake2[i] == 0:
            del cake2[i]
        if len(cake1) == len(cake2.keys()):
            ans += 1
    return ans