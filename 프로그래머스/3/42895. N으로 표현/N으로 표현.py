def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)] # 최솟값이 8보다 크면 -1리턴이므로? N <= 9 이므로?
    
    for i in range(1, len(dp)):
        dp[i].add(int(str(N) * i)) # N을 반복해서 만들 수 있는 숫자 저장
    
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        
        # 목표 숫자가 해당 단계에서 만들어졌다면, 해당 i를 반환
        if number in dp[i]:
            return i
    
    return -1