import sys
import math
input = sys.stdin.readline

N = int(input())  # 시험장 개수
A = list(map(int, input().split()))  # 각 시험장에 있는 응시자의 수
# 총감독관과 부감독관이 한 시험장에서 감시할 수 있는 응시자의 수
B, C = map(int, input().split())

# 총감독관은 무조건 시험장마다 1명씩 배치함
ans = N
        
for i in range(N):
    # 총감독관이 맡고 남은 인원(음수인 경우는 0으로 처리)
    needed = max(0, A[i] - B)
    # 필요한 부감독관 수
    ans += math.ceil(needed / C)

# 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수 출력      
print(ans)