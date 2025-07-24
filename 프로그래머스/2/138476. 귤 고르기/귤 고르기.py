from collections import Counter

def solution(k, tangerine):
    # 개수 기준 내림차순 정렬
    sorted_tangerine = sorted(Counter(tangerine).items(), key=lambda x:x[1], reverse=True)

    types = 0
    nums = 0
    
    for t, n in sorted_tangerine:
        nums += n
        types += 1
        
        if nums >= k:
            return types