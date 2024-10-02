def solution(num_list, n):
    return [num_list[idx:idx + n] for idx in range(0, len(num_list), n)]