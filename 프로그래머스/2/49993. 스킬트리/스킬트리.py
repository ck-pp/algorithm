def solution(skill, skill_trees):
    ans = 0
    for sk in skill_trees:
        tf = 1
        st = list(skill)
        for s in sk:
            if s in st:
                if s != st[0]:
                    tf = 0
                    break
                else:
                    st.pop(0)
        if tf:
            ans += 1
    return ans