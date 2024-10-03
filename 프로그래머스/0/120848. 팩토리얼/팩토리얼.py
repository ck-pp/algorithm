def solution(n):
    fact = 1
    for num in range(2, 11):
        if fact * num > n:
            return num - 1
        fact *= num
        
    return num