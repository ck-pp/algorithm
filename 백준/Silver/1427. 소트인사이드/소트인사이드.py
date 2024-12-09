import sys
imput = sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    for num in arr:
        if num > pivot:
            left.append(num)
        elif num < pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quick_sort(left) + equal + quick_sort(right)

N = list(map(int, list(input())))

sorted_N = quick_sort(N)
print(''.join(map(str, sorted_N)))