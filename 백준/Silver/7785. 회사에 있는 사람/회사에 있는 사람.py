import sys
input = sys.stdin.readline

n = int(input())
informations = list(tuple(input().strip().split()) for _ in range(n))
    
in_company = {}
for name, info in informations:
    if info == 'enter':
        in_company[name] = True
    else:  # 'leave'
        del in_company[name]
        
sorted_name = sorted(in_company.keys(), reverse=True)
for name in sorted_name:
    print(name)