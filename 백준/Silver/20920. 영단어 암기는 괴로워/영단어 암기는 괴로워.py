import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input().strip()
    
    if len(word) >= M:
        if word in words:  # 딕셔너리에 단어가 존재하는 경우
            words[word] += 1
        else:  # 딕셔너리에 단어가 존재하지 않는 경우
            words[word] = 1

# 단어 빈도수 기준 내림차순 -> 단어 길이 기준 내림차순 -> 단어 사전순
sorted_words = sorted(words.items(), key=lambda item:(-item[1], -len(item[0]), item[0]))

for w, _ in sorted_words:
    print(w)