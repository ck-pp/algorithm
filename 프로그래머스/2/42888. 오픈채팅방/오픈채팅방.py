def solution(record):
    ans = []
    id_name = {}
    
    for idx in range(len(record)):
        r = record[idx]
        st_list = r.split(" ")
        # [0]: action / [1]: id / [2]: 닉네임(퇴장시, X)
        if st_list[0] == 'Enter':
            id_name[st_list[1]] = st_list[2]
        elif st_list[0] == 'Change':
            id_name[st_list[1]] = st_list[2]
            record[idx] = ""
            
    for st in record:
        st_list = st.split(" ")
        if st_list[0] == 'Enter':
            ans.append(id_name[st_list[1]] + "님이 들어왔습니다.")
        elif st_list[0] == 'Leave':
            ans.append(id_name[st_list[1]] + "님이 나갔습니다.")
    return ans