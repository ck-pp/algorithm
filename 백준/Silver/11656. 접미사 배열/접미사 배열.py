import sys
input = sys.stdin.readline

word = input().strip()
res = []

for i in range(len(word)):
    res.append(word[i:])
    
res.sort()
for suffix in res:
    print(suffix)