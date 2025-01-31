import sys
input = sys.stdin.readline

def Rev(num_s):
    reverse_n = int(''.join(list(reversed(num_s))))
    return reverse_n
    
X, Y = input().strip().split()

# 정답 출력
print(Rev(str(Rev(X) + Rev(Y))))