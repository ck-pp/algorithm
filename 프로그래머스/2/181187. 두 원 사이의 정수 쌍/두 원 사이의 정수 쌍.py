from math import pow, sqrt, floor, ceil

def solution(r1, r2):
    ans = r2 - r1 + 1
    for x in range(1, r2):
        max_y = floor(sqrt(pow(r2, 2) - pow(x, 2)))
        if x < r1:
            min_y = ceil(sqrt(pow(r1, 2) - pow(x, 2)))
        else:
            min_y = 1
        ans += (max_y - min_y + 1)
    return ans * 4