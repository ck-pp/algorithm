def solution(brown, yellow):
    ans = []
    for i in range(1, int(yellow**(1/2))+1):
        div = yellow/i
        if (i+2)*2 + div*2 == brown:
            ans.extend([div+2, i+2])
    return ans