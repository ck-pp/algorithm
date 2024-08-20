def solution(numbers):
    for idx, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(idx))
        
    return int(numbers)