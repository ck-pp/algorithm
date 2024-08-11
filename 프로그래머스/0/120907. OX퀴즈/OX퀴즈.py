def solution(quiz):
    ans = []
    for q in quiz:
        num1, op, num2, eq, res = q.split(' ')
        right = "X"
        if op == '-':
            if int(num1) - int(num2) == int(res):
                right = "O"
        else:
            if int(num1) + int(num2) == int(res):
                right = "O"
        ans.append(right)
        
    return ans