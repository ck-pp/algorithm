import sys
input = sys.stdin.readline

N = int(input())
serial_nums = [input().strip() for _ in range(N)]

# 길이 짧은 것 -> 자리 수 합 작은 것(숫자만) -> 사전순
serial_nums.sort(key=lambda s:(len(s), sum(int(c) for c in s if c.isnumeric()), s))

for s in serial_nums:
    print(s)