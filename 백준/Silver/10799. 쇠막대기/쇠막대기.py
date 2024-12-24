import sys
input = sys.stdin.readline

parentheses = list(input().strip())
n = len(parentheses)

stack = []  # (괄호 문자, 인덱스)
total_pieces = 0
for i in range(n):
        if parentheses[i] == '(':
            stack.append('(')
        else:  # ')'
            if stack:
                stack.pop()
            if parentheses[i - 1] == '(':  # 레이저
                total_pieces += len(stack)
            else:  # 막대기 끝
                total_pieces += 1

print(total_pieces)