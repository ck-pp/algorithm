from collections import Counter

def solution(k, tangerine):
    tengerine_per_size = Counter(tangerine)  # (사이즈: 개수) 딕셔너리
    sorted_t = sorted(tengerine_per_size.items(), key=lambda x: x[1], reverse=True)  # 개수별(value 기준)로 내림차순 정렬
    
    ans, cur_cnt = 0, 0
    for size, cnt in sorted_t:
        ans += 1
        cur_cnt += cnt
        # 현재 담은 오렌지의 개수가 k를 넘어가면 종료
        if cur_cnt >= k:
            break
            
    return ans