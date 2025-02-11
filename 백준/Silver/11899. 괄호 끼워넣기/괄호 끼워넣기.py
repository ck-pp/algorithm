import sys
input = sys.stdin.readline

S = input().strip()
stack = []
ans = 0

for i in range(len(S)):
    # 열린 괄호인 경우
    if S[i] == '(':
        stack.append('(')
    # 닫힌 괄호인 경우
    else:
        if not stack:  # 잘못된 괄호 문자열, 앞에 열린 괄호 추가해야 하는 경우
            ans += 1
        else:
            stack.pop()

# 잘못된 괄호 문자열, 뒤에 닫힌 괄호 추가해야 하는 경우
ans += len(stack)

# 앞과 뒤에 붙여야 할 괄호의 최소 개수 출력
print(ans)