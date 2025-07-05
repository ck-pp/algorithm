def solution(nums):
    # N/2마리, 최대 많은 종류
    N = len(nums)
    poketmon_set = set(nums)
    n = len(poketmon_set)
    select_num = N // 2
    
    return select_num if n > select_num else n
    