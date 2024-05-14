def solution(storey):
    ans = 0
    while storey > 0:
        if storey % 10 > 5:
            ans += (10 - (storey % 10))
            storey = storey // 10 + 1
        elif storey % 10 == 5:
            ans += 5
            if (storey // 10) % 10 >= 5:
                storey = (storey + 5) // 10
            else:
                storey //= 10
        else:
            ans += (storey % 10)
            storey //= 10
    return ans