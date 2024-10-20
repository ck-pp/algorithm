import sys

N = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for _ in range(N)]

sorted_list = sorted(list(set(word_list)), key=lambda x:(len(x), x))
for word in sorted_list:
    print(word)