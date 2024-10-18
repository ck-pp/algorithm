def solution(prices):
    # 초 단위 주식 가격 배열
    # 가격이 떨어지지 않은 기간
    stack = []
    ans = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        while len(stack) > 0 and stack[-1][1] > prices[i]:
            prev, _ = stack.pop()
            ans[prev] = i - prev
        stack.append((i, prices[i]))  # (현재 시점, 주식 가격)
    
    for i, price in stack:  # 스택에 값 남아있는 경우(가격이 떨어지지 않음)
        ans[i] = len(prices) - i - 1
        
    return ans