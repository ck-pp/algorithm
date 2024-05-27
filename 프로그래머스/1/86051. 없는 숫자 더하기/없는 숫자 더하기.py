def solution(numbers):
    sum_n = sum([n for n in range(10)])
    for num in numbers:
        sum_n -= num
    return sum_n