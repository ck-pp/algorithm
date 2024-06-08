def solution(num):
    steps = 0
    while num > 1 and steps < 500:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        steps += 1
    if num > 1:
        return -1
    return steps