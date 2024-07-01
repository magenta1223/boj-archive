#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20529                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20529                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 19:53:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from itertools import combinations as combs 
 
def _dist(a,b):
    return sum([t1 != t2  for t1, t2 in zip(a,b)])
 
def dist(a,b,c):
    a,b,c = MBTI[a], MBTI[b], MBTI[c]
    return DISTS[a][b] + DISTS[b][c] + DISTS[c][a]
 
ALL_MBTIS = 'ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP, ESTJ, ESFJ, ENFJ, ENTJ'
ALL_MBTIS = ALL_MBTIS.split(", ") 
DISTS = {mbti : {_mbti : _dist(mbti, _mbti) for _mbti in ALL_MBTIS} for mbti in ALL_MBTIS}
 
INF = 13
 
for _ in range(int(input())):
    N = int(input())
    MBTI = input().split()
    # 가장 가까운 세 명
    d = INF
    for a,b,c in combs(list(range(N)), 3):
        _d = dist(a,b,c)
        if d > _d:
            d = _d 
        if _d == 0:
            break 
    print(d)