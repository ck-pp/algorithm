import sys

nums = [sys.stdin.readline() for _ in range(3)]

for num in nums:
    con_nums = []
    cnt = 1
    for i in range(1, len(num)):
        if num[i] == num[i-1]:
            cnt += 1
        else:
            con_nums.append(cnt)
            cnt = 1
        
    print(max(con_nums))