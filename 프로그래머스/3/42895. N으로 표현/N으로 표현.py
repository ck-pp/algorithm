def solution(N, number):
    # N을 한 번만 써도 되는 경우
    if N == number:
        return 1
    
    # dp 정의
    # dp[i]: N을 i번 사용해서 만들 수 있는 모든 정수 집합
    dp = [set() for _ in range(9)]
    
    # 1. N을 이어붙인 값
    for k in range(1, 9):
        dp[k].add(int(str(N) * k))

        # 2. 사칙연산
        for a in range(1, k):
            b = k - a
            for x in dp[a]:
                for y in dp[b]:
                    dp[k].add(x + y)
                    dp[k].add(x - y)
                    dp[k].add(x * y)
                    if y != 0:
                        dp[k].add(x // y)
        
        # k는 1부터 시작이므로 처음 이 조건을 만족한 k가 최솟값
        if number in dp[k]:
            return k
    
    # 최솟값이 8보다 크면
    return -1