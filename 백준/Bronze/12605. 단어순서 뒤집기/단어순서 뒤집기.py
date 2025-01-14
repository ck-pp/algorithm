import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    words = list(input().strip().split())
    
    words.reverse()
    print("Case #" + str(i) + ': ' + ' '.join(words))