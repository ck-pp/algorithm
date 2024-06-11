def solution(numbers, target):
    def dfs(idx, cur_sum):
        if idx == len(numbers):
            return 1 if cur_sum == target else 0
        return dfs(idx + 1, cur_sum + numbers[idx]) + dfs(idx + 1, cur_sum - numbers[idx])
    
    return dfs(0, 0)