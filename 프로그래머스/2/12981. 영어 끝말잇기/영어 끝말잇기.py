def solution(n, words):
    used_word = set([words[0]])
    ans = [0, 0]
    for i in range(1, len(words)):
        cur_word = words[i]
        if words[i-1][-1] != cur_word[0] or cur_word in used_word:
            ans[0] = (i % n) + 1  # 탈락자 번호
            ans[1] = (i // n) + 1  # 탈락자 차례
            break

        # 중복 체크 위해 사용된 단어 리스트에 현재 단어 추가
        used_word.add(cur_word)

    return ans