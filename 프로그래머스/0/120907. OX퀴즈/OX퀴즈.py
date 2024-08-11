def solution(quiz):
    ans = []
    for q in quiz:
        num1, op, num2, eq, res = q.split(' ')
        if op == '-':
            right = "O" if int(num1) - int(num2) == int(res) else "X"
            ans.append(right)
        else:
            right = "O" if int(num1) + int(num2) == int(res) else "X"
            ans.append(right)
        
    return ans