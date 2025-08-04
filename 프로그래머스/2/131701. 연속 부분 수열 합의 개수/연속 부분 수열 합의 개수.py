def solution(elements):
    sums = set(elements)
    n = len(elements)
    
    # 최대 한바퀴이므로 배열을 2번 반복한다.
    elements.extend(elements)
    
    for i in range(n):
        for j in range(2, n):
            sums.add(sum(elements[i:i+j]))
            
    sums.add(sum(elements))
    
    return len(sums)
    