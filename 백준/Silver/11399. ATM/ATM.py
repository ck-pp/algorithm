import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left, equal, right = [], [], []
    pivot = arr[len(arr) // 2]
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quick_sort(left) + equal + quick_sort(right)

sorted_times = quick_sort(times)
sum_t = 0
for i in range(N):
    sum_t += (N-i) * sorted_times[i]

print(sum_t)