def merge_sort(arr): # 반으로 나누어 재귀적으로 정렬
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right): # 병합
    res = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if (left[i] > right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        
    res.extend(left[i:])
    res.extend(right[j:])
        
    return res

def solution(citations):
    sorted_citations = merge_sort(citations) # 병합 정렬(내림차순)
    h_idx = 0
    for i, citation in enumerate(sorted_citations):
        if citation >= i + 1:
            h_idx = i + 1
        else:
            break
        
    return h_idx
    