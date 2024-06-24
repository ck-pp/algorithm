def solution(price, money, count):
    need_m = sum([n for n in range(1, count+1)]) * price
    if money - need_m < 0:
        return need_m - money
    else:
        return 0