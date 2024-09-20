def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    for num in arr:
        if num < pivot:  # 오름차순 정렬
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quick_sort(left) + equal + quick_sort(right)

def solution(num_list):
    sorted_list = quick_sort(num_list)
    
    return sorted_list[5:]