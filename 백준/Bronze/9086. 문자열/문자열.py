import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = list(input().strip())
    
    print(string[0] + string[-1])  # 두 글자 붙여서 출력(+)