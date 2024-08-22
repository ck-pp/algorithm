def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x + pivot > pivot + x]
    equal = [x for x in arr if x + pivot == pivot + x]
    right = [x for x in arr if x + pivot < pivot + x]
    
    return quick_sort(left) + equal + quick_sort(right)

def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_numbers = quick_sort(numbers)
    ans = ''.join(sorted_numbers)
    
    return str(int(ans))