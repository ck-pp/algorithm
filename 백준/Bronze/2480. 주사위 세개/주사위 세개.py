import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())  # 3개의 눈
deduplication = list(set([A, B, C]))  # 중복 제거
arr = [A, B, C]

# 3개의 눈이 모두 같은 경우
if A == B == C:
    print(10000 + A * 1000)

# 3개의 눈이 모두 다른 경우
elif A != B and B != C and A != C:
    print(max(A, B, C) * 100)

# 같은 눈이 2개만 나오는 경우
else:
    for num in deduplication:
        arr.remove(num)
    # arr에 남은 값이 중복되는 값
    print(1000 + arr[0] * 100)