def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    
    for num in arr:  # 오름차순 정렬
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quick_sort(left) + equal + quick_sort(right)

def solution(array, commands):
    ans = []
    for i, j, k in commands:
        sorted_arr = quick_sort(array[i-1:j])
        ans.append(sorted_arr[k-1])
        
    return ans