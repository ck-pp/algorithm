def solution(num_list, n):
    ans = []
    for idx in range(n, len(num_list) + 1, n):
        ans.append(num_list[idx - n:idx])
    return ans