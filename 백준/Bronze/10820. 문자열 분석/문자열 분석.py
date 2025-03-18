import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    
    # 소문자, 대문자, 숫자, 공백 카운트
    lower_count = 0
    upper_count = 0
    digit_count = 0
    space_count = 0
    
    for ch in line:
        if ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif ch == ' ':
            space_count += 1
    
    print(lower_count, upper_count, digit_count, space_count)