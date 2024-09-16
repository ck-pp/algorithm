def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    
    for num in arr:
        if num > pivot:  # 내림차순 정렬
            left.append(num)
        elif num < pivot:
            right.append(num)
        else:
            equal.append(num)
            
    return quick_sort(left) + equal + quick_sort(right)

def solution(citations):
    sorted_citations = quick_sort(citations)
    h_idx = 0
    
    for i, c in enumerate(sorted_citations):
        if c >= i + 1:  # i가 배열 인덱스이므로 +1
            h_idx = i + 1
        else:
            break
        
    return h_idx