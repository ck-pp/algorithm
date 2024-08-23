def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot] # 부등호에 따라 내림차순/오름차순 정렬할 수 있다.
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    
    return quick_sort(left) + equal + quick_sort(right)

def solution(citations):
    sorted_citations = quick_sort(citations) # 퀵 정렬(내림차순)
    h_idx = 0
    for i, citation in enumerate(sorted_citations):
        if citation >= i + 1:
            h_idx = i + 1
        else:
            break
        
    return h_idx