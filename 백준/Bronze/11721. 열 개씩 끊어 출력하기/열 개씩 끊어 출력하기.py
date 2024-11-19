import sys
input = sys.stdin.readline

words = input().strip()
i = 0

while len(words) - i >= 10:
    print(words[i:i+10])
    i += 10

if len(words) - i < 10:
    print(words[i:])