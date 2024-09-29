def solution(arr):
    ans = []
    for a in arr:
        ans.extend([a] * a)
    return ans