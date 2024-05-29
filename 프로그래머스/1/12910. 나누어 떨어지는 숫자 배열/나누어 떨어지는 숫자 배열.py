def solution(arr, divisor):
    ans = []
    for n in arr:
        if n % divisor == 0:
            ans.append(n)
    if not ans:
        return [-1]
    return sorted(ans)