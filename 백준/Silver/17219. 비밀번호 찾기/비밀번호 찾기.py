import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 저장된 사이트 주소 개수, 비밀번호 찾으려는 사이트 개수
site_pws = {}  # 사이트 도메인 주소: 비밀번호
for _ in range(N):
    site_domain, pw = input().strip().split()
    site_pws[site_domain] = pw
    
for _ in range(M):
    find_domain = input().strip()
    print(site_pws[find_domain])