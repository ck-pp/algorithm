import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

res = [-1] * N
stack = []  # 아직 오큰수를 찾지 못한 인덱스 저장
for i in range(N):
    # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 인덱스가 가리키는 숫자보다 큰 경우
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        res[idx] = nums[i]  # 해당 인덱스의 오큰수를 현재 숫자로 설정
        
    stack.append(i)

# 스택에 남아 있는 인덱스는 이미 -1로 초기화되어 있음
print(*res)