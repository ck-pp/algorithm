import math

def solution(progresses, speeds):
    ans = []
    w_period = []
    stack = []
    for i in range(len(progresses)):
        period = math.ceil((100 - progresses[i]) / speeds[i])
        w_period.append(period)
    for j in w_period:
        if len(stack) > 0 and stack[0] < j:
            ans.append(len(stack))
            stack.clear()
        stack.append(j)
    ans.append(len(stack))
    return ans