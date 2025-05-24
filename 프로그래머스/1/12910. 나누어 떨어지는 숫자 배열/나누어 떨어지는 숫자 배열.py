def solution(arr, divisor):
    ans = sorted([num for num in arr if num % divisor == 0])
    if ans:
        return ans
    else:
        return [-1]