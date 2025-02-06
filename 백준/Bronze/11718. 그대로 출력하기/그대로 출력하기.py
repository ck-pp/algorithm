import sys
input = sys.stdin.readline

while True:
    words = input().strip()
    if words == '':
        break
    else:
        print(''.join(words))