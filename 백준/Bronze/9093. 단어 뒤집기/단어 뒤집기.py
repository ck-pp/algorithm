import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    words = input().strip().split()
    
    for i in range(len(words)):
        words[i] = ''.join(list(reversed(words[i])))

    print(' '.join(words))