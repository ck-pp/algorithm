def solution(arr, divisor):
    ans = []
    for n in arr:
        if n % divisor == 0:
            ans.append(n)
    return sorted(ans) or [-1]