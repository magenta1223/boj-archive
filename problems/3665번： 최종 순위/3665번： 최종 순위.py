#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3665                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3665                          #+#        #+#      #+#     #
#     Solved: 2024-04-12 19:09:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
 
input = open(0).readline 
 
for _ in range(int(input())):
    N = int(input())
    T = list(map(int,input().split()))
    M = int(input())
    
    d = dict()
    connect = {i : [] for i in range(1,N+1)}
    count = {i : 0 for i in range(1,N+1)}
    for i in range(N):
        for j in range(i+1, N):
            connect[T[i]].append(T[j])
            count[T[j]] += 1 
            
    connect_tmp = {i : [] for i in range(1,N+1)}
    count_tmp = {i : 0 for i in range(1,N+1)}
    for _ in range(M):
        a,b = map(int,input().split())
        if count[a] < count[b]:
            a,b = b,a
        connect_tmp[a].append(b)
        count_tmp[b] += 1 
        if a in connect[b]:
            connect[b].remove(a)
            count_tmp[a] -= 1  
 
    for i in range(1,N+1):
        if count_tmp[i]:
            count[i] += count_tmp[i]
        if connect_tmp[i]:
            connect[i].extend(connect_tmp[i])
 
    # 위상정렬을 하는데, a b에 해당하는 쌍만 바꿔서 해야된다.
    # 위상정렬이 불가능한 경우
    # count, connect 
    # 서로의 connect에 포함이 되는 경우 -> 불가능
    # 큐의 크기가 2 이상인 경우 -> ? 
 
 
    ans = []
    q = deque([i for i in range(1,N+1) if not count[i]])
    deterministic = True
    while q and deterministic:
        x = q.popleft()
        ans.append(x)
        for nx in connect[x]:
            if count[nx]:
                count[nx] -= 1 
                if not count[nx]:
                    q.append(nx)
 
        if len(q) > 1:
            deterministic = False 
 
    if not deterministic:
        print("?")
    elif len(ans) != N:
        print("IMPOSSIBLE")
    else:
        print(*ans)