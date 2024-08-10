def solution(numbers, target):
    def dfs(idx, c_sum):
        if idx == len(numbers):
            return 1 if c_sum == target else 0
        return dfs(idx + 1, c_sum + numbers[idx]) + dfs(idx + 1, c_sum - numbers[idx])
    
    return dfs(0, 0)