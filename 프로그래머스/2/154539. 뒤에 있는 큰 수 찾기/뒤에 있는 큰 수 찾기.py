def solution(numbers):
    ans = [0] * len(numbers)
    stack = []
    
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            ans[stack.pop()] = num
        stack.append(idx)
        
    for r in stack:
        ans[r] = -1
        
    return ans