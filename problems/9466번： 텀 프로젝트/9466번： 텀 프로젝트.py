#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9466                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9466                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 17:29:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
for _ in range(int(input())):
    N = int(input())
    L = [0] + list(map(int,input().split()))
    visited = [False] * (N+1)
    ans = N
    for a in range(1, N+1):
        if visited[a]:
            continue
        visited[a] = True 
        cycle = [a]
        while not visited[L[a]]:
            a= L[a]
            visited[a] = True 
            cycle.append(a)
        
        if L[a] in cycle:
            ans -= len(cycle) - cycle.index(L[a]) # cycle start 
 
    print(ans)