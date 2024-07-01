#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15666                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15666                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 13:11:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
visited = set()
def dfs(bitmask,prev_i,l):
    if len(l) == M:
        print(*l)
        return
    for i in range(prev_i,N):
        nextl = tuple(l+[L[i]])
        if nextl in visited:
            continue 
        visited.add(nextl)
        dfs(bitmask|(1<<i),i,l+[L[i]])
dfs(0,0,[])