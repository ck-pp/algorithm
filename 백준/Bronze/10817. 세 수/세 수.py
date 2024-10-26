import sys

abc_list = list(map(int, sys.stdin.readline().split()))
abc_list.sort()

print(abc_list[1])