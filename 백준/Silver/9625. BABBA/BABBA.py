import sys
input = sys.stdin.readline

K = int(input())

replace_word = {'A': [0, 1], 'B': [1, 1]}
dp = [[0, 0]] * (K + 1)  # [A의 개수, B의 개수]
dp[0] = [1, 0]

for i in range(1, K+1):
    cur_A = [dp[i-1][0] * replace_word['A'][0], dp[i-1][0] * replace_word['A'][1]]
    cur_B = [dp[i-1][1] * replace_word['B'][0], dp[i-1][1] * replace_word['B'][1]]
    
    dp[i] = [cur_A[0]+cur_B[0], cur_A[1]+cur_B[1]]
    
print(*dp[K])