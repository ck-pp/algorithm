def solution(elements):
    sums = set(elements)  # 초기화(길이 1인 부분 수열 합)
    
    n = len(elements)
    # 최대 한바퀴이므로 배열을 2번 반복한다. (= 메모리 성능 이슈)
    elements.extend(elements)
    for i in range(2, n):
        for j in range(n):
            sums.add(sum(elements[j:j+i]))
            
    sums.add(sum(elements))  # 길이 n인 부분 수열 = 수열 자체 합은 1번만 구해서 더하도록 함
    
    return len(sums)
    