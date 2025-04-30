from collections import defaultdict

def solution(genres, plays):
    ans = []
    n = len(genres)  # 수록곡 개수
    
    # 장르별 재생 횟수
    plays_by_genre = defaultdict(int)
    # 장르별 수록곡 번호
    songs_by_genre = defaultdict(list)
    
    for i in range(n):
        songs_by_genre[genres[i]].append((i, plays[i]))
        plays_by_genre[genres[i]] += plays[i]

    # 재생 횟수 기준 수록곡 내림차순 정렬, 고유 번호 기준 수록곡 오름차순 정렬
    for j in songs_by_genre:
        songs_by_genre[j].sort(key=lambda x:(-x[1], x[0]))
    
    # 총 재생 횟수 개수 기준 장르 내림차순 정렬
    sorted_genre = sorted(plays_by_genre.items(), key=lambda item:-item[1])
    
    for genre, _ in sorted_genre:
        # 장르에 속한 곡이 1곡인 경우
        if len(songs_by_genre[genre]) < 2:
            ans.append(songs_by_genre[genre][0][0])
        # 장르에 속한 곡이 2곡 이상인 경우
        else:
            for j in range(2):
                ans.append(songs_by_genre[genre][j][0])    
    
    return ans