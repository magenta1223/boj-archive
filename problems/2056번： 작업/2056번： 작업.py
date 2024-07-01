#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2056                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2056                          #+#        #+#      #+#     #
#     Solved: 2024-06-13 12:37:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
INF = float("inf")
N = int(input())
PreReq = [[] for _ in range(N)]
T = [INF] * N
COSTS=[INF]*N 
for i in range(N):
    l = list(map(int,input().split()))
    t, l = l[0], l[1:]
    T[i] = t 
    if l[0]:
        for j in range(l[0]):
            PreReq[i].append(l[j+1]-1)
    else:
        COSTS[i] = t 
 
for _ in range(N):
    for i in range(N):
        # i번째 작업의 갱신
        if COSTS[i] != INF:
            continue  
        res = 0
        for pretask in PreReq[i]:
            res = max(res, COSTS[pretask])
        COSTS[i] = res + T[i]
print(max(COSTS))
 