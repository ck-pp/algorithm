import heapq as hq

def solution(k, score):
    top_k = []  # min-heap
    ans = []
    for s in score:
        if len(top_k) >= k:
            if top_k[0] < s:
                hq.heappop(top_k)
                hq.heappush(top_k, s)
        
        else:  # len(top_k) < k
            hq.heappush(top_k, s)
            
        ans.append(top_k[0])
        
    return ans
        
    
            
            
    