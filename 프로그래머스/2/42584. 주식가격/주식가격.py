from collections import deque

def solution(prices):
    ans = deque([])
    len_prices = len(prices)
    for i in range(len_prices):
        cnt = 0
        for j in range(i+1, len_prices):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        ans.append(cnt)
    return list(ans)