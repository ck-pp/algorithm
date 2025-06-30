def solution(n, words):
    turns = 0  # 현재 턴 수
    used_words = []
    for w in words:
        # 1) 이미 나온 단어이거나 
        # 2) 앞사람이 말한 단어의 마지막 문자로 시작하는 단어가 아닌 경우
        if w in used_words or (used_words and used_words[-1][-1] != w[0]):
            return (turns % n + 1, turns // n + 1)
        
        used_words.append(w)
        turns += 1
        
    return [0, 0]
        