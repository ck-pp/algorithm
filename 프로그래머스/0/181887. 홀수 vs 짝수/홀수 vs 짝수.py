def solution(num_list):
    odd = [num_list[idx] for idx in range(len(num_list)) if (idx+1) % 2 > 0]
    even = [num_list[idx] for idx in range(len(num_list)) if (idx+1) % 2 == 0]
    return max(sum(odd), sum(even))