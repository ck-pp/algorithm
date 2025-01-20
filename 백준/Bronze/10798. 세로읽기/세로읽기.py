import sys
input = sys.stdin.readline

string = [input().strip() for _ in range(5)]
length = [len(s) for s in string]
max_len = max(length)

for i in range(max_len):
    for j in range(5):
        if i < len(string[j]):
            print(string[j][i], end="")