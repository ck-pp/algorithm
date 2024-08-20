def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]) <= 0:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res

def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_numbers = merge_sort(numbers)
    ans = ''.join(sorted_numbers)
    
    return str(int(ans))