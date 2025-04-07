import sys
input = sys.stdin.readline

arr = []
max_n = 0
while True:
    n = int(input())
    
    # 입력이 0일 경우 종료
    if n == 0:
        break
    arr.append(n)
    
    # 입력값 중 최댓값 업데이트
    if max_n < n:
        max_n = n
    
# 1. dp 정의
# ways[full][half] = (full, half) 상태에서 만들 수 있는 W/H 문자열의 개수
ways = [[-1]* (max_n + 1) for _ in range(max_n + 1)]

# 2. dp 값 계산
def count_ways(full, half):
    # 만약 통째 알약이 하나도 없다면, 남은 half만큼 H를 쭉 꺼내는 1가지 방법밖에 없음
    if full == 0:
        return 1
        
    # 이미 계산된 값 있으면 그대로 반환
    if ways[full][half] != -1:
        return ways[full][half]
        
    # 통째 알약 하나 꺼내는 경우(재귀)
    res = count_ways(full-1, half+1)
    
    # 반 알이 남아있다면
    if half > 0:
        res += count_ways(full, half-1)
    
    ways[full][half] = res
    return res
    
# 3. 각 테스트 케이스에 대해 가능한 문자열의 개수 출력
# # count_ways 함수 내에서 ways 테이블이 채워질 것이므로 중복 호출시에도 빠르다.
for n in arr:
    print(count_ways(n, 0))