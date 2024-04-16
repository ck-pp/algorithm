from collections import Counter

def solution(k, tangerine):
    ans = 0
    cnt = 0
    dict_t = Counter(tangerine)
    sort_v = sorted(dict_t.values(), reverse=True)
    while cnt < k:
        cnt += sort_v[ans]
        ans += 1
    return ans