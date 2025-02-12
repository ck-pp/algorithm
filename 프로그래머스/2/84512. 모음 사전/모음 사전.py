from itertools import product

def solution(word):
    # 중복 순열
    alphas = ['A', 'E', 'I', 'O', 'U']
    words = []  # 사전
    for i in range(1, 6):
        words.extend(list(product(alphas, repeat=i)))
    
    # 현재 사전은 튜플 형태로 저장되어 있으므로 문자열로 변환해 저장할 사전 따로 정의
    str_words = []
    ans = 0
    for tup in words:
        str_words.append(''.join(tup))
    
    str_words.sort()  # 사전 정렬
    ans += (str_words.index(word) + 1)  # 인덱스는 0부터 시작하므로 인덱스 + 1
    
    # 주어진 단어의 순서 출력
    return ans