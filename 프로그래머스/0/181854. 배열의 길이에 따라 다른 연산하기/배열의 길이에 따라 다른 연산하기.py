def solution(arr, n):
    for i in range((len(arr) + 1) % 2, len(arr), 2):
        arr[i] += n
    return arr