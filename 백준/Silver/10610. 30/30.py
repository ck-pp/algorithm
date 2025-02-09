import sys
input = sys.stdin.readline

# 정수 리스트 형태로 저장
N = list(map(int, list(input().strip())))

def is_multiple(arr):
    
    N.sort(reverse=True)
    
    # 30의 배수가 되려면? 
    # 1) 각 자릿수의 합이 3의 배수여야 한다.
    # 2) 마지막 자릿수가 0이여야 한다.
    if sum(arr) % 3 == 0 and N[-1] == 0:
        return int(''.join(map(str, N)))
    
    else:
        return -1
        
print(is_multiple(N))