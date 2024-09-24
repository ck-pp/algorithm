def quick_sort(arr, n):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    
    def sort_key(x):
        # 첫 번째 기준: n으로부터의 거리
        # 두 번째 기준: 거리가 같다면 더 큰 숫자가 앞에 위치하도록
        # 기본이 오름차순이므로, -를 붙여서 내림차순으로 정렬
        return (abs(x - n), -x)
    
    # 튜플끼리 비교: 첫 번째 원소끼리 비교 -> 동일하면 두 번째 원소끼리 비교 
    left = [x for x in arr if sort_key(x) < sort_key(pivot)]
    middle = [x for x in arr if sort_key(x) == sort_key(pivot)]
    right = [x for x in arr if sort_key(x) > sort_key(pivot)]
    
    return quick_sort(left, n) + middle + quick_sort(right, n)

def solution(numlist, n):
    return quick_sort(numlist, n)