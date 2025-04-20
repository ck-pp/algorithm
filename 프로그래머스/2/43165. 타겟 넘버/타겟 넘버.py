def solution(numbers, target):
    n = len(numbers)
    
    # 1. dfs 정의
    def dfs(idx, sum_val):
        # 모든 정수를 연산에 사용한 경우
        if idx == n:
            # 타겟 넘버가 만들어지면 방법의 수 + 1
            return 1 if sum_val == target else 0
        
        # 다음 숫자를 더하고 빼서 재귀 호출
        return dfs(idx+1, sum_val + numbers[idx]) + dfs(idx+1, sum_val - numbers[idx])
    
    # 2. dfs 호출
    return dfs(0, 0)