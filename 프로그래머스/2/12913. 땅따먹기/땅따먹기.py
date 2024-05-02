def solution(land):
    ans = 0
    for i in range(1, len(land)):
        # land[1][0] += max(land[0][1], land[0][2], land[0][3])
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        # land[1][1] += max(land[0][2], land[0][3], land[0][0])
        land[i][1] += max(land[i-1][2], land[i-1][3], land[i-1][0])
        land[i][2] += max(land[i-1][3], land[i-1][0], land[i-1][1])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[-1])