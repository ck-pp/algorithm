import sys
input = sys.stdin.readline

nums = []
for _ in range(28):
    nums.append(int(input()))
    
nums.sort()  # 오름차순 정렬

for i in range(1, 31):
    # 제출하지 않은 출석 번호 출력
    if i not in nums:
        print(i)