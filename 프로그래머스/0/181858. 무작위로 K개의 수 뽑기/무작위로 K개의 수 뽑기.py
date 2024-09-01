def solution(arr, k):
    res_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] not in res_arr:
            res_arr.append(arr[i])
    res_arr.extend([-1] * (k - len(res_arr)))
    return res_arr[:k]