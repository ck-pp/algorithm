def solution(elements):
    ans = []
    elements.extend(elements)
    for i in range(len(elements)//2):
        sum = elements[i]
        for j in range(1, len(elements)//2+1):
            ans.append(sum)
            sum += elements[i+j]
    return len(set(ans))