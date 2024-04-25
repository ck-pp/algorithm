def solution(s):
    ans = 0
    q = list(s)
    stack = []
    dict = {'{':'}', '(':')', '[':']'}
    for i in q:
        temp_q = q
        for j in temp_q:
            if j in dict.keys():
                stack.append(j)
            else:
                if stack and j == dict[stack[-1]]:
                    stack.pop()
                else:
                    stack.clear()
                    ans += 1
                    break
        if stack:
            ans += 1
        q.append(q.pop(0))
    return len(q) - ans