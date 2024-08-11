def solution(rank, attendance):
    t_student = []
    for i in range(len(attendance)):
        idx_rank = []
        if attendance[i] == True:
            t_student.append([i, rank[i]])
    t_student.sort(key=lambda x:x[1])
    return 10000 * t_student[0][0] + 100 * t_student[1][0] + t_student[2][0]