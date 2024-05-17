def solution(k, ranges):
    ans = []
    area = []
    xy = [[0, k]]
    n = 0
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        xy.append([n, k])
        n += 1
    for idx in range(1, len(xy)):
        area.append((xy[idx][1]+xy[idx-1][1])/2)
    for r in ranges:
        if n+r[1] - r[0] < 0:
            ans.append(-1)
        else:
            ans.append(sum(area[r[0]:n+r[1]]))
    return ans