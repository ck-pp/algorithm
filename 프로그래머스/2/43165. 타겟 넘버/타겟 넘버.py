from collections import Counter

def solution(numbers, target):
    # 가능한 모든 해를 찾아야 함 = DP로 풀이해보기
    n = len(numbers)
            
    # 1. dp 정의
    # dp[i]: i번째 수까지 더하거나 빼서 만들 수 있는 숫자 리스트
    dp = [[] for _ in range(n)]
    dp[0].extend([numbers[0], -numbers[0]])
    
    # 2중 for문인게 조금 걸리긴 한다... O((n-1)*2^n)
    # 메모리 사용도!
    for i in range(1, n):
        for num in dp[i-1]:
            dp[i].extend([num - numbers[i], num + numbers[i]])
    
    # 모든 정수들을 사용해 더하거나 빼서 target 넘버를 만들 수 있는 경우의 수
    return Counter(dp[n-1])[target]