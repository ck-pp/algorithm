import sys
input = sys.stdin.readline

N = int(input())
new_num = N
cycles = 0

while True:
    a = new_num // 10
    b = new_num % 10
    
    # 새로운 수
    new_num = b * 10 + (a + b) % 10
    cycles += 1
    
    # 원래 수로 돌아온 경우
    if new_num == N:
        break

# N의 사이클 길이 출력
print(cycles)