import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left, equal, right = [], [], []
    pivot = arr[len(arr)//2]
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quick_sort(left) + equal + quick_sort(right)

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]

sorted_list = quick_sort(num_list)
for num in sorted_list:
    print(num)