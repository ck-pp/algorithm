def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    
    for num in arr:
        if num + pivot > pivot + num:
            left.append(num)
        elif num + pivot < pivot + num:
            right.append(num)
        else:
            equal.append(num)
            
    return quick_sort(left) + equal + quick_sort(right)

def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_numbers = ''.join(quick_sort(numbers))
    
    return str(int(sorted_numbers))  # 맨앞? 0이 (여러개) 붙을 경우