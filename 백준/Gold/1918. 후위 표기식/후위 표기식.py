import sys
input = sys.stdin.readline

notation = list(input().strip())
operator = []  # 연산자
result = []  # 후위 표기법 결과

# 연산자 우선순위 함수
def precedence(op):
    if op == '(':
        return 0
    elif op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return -1

for n in notation:
    if n.isalpha():  # 피연산자일 경우
        result.append(n)
    elif n == '(':
        operator.append(n)
    elif n == ')':
        # 여는 괄호 만날 때까지 스택에서 연산자 꺼내 result에 추가
        while operator and operator[-1] != '(':
            result.append(operator.pop())
        operator.pop()  # 여는 괄호 제거
    else:  # 연산자일 경우
        # 현재 연산자보다 우선순위가 높거나 같은 연산자를 result로 이동
        while operator and precedence(operator[-1]) >= precedence(n):
            result.append(operator.pop())
        operator.append(n)  # 현재 연산자 추가
        
# 스택에 남아있는 연산자 처리
while operator:
    result.append(operator.pop())
        
print(''.join(result))