#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15663                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15663                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 23:50:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int,input().split())
L = list(map(int,input().split()))
L.sort()
 
ans = set()
 
def dfs(bitmask, l):
    global ans 
    if sum(map(int, list(bin(bitmask)[2:]))) == M:
        ans.add(tuple(l))
        return 
    
    for i in range(N):
        if (1<<i) & bitmask:
            continue
        dfs(bitmask|(1<<i), l + [L[i]])
 
dfs(0, [])
for a in ans:
    print(*a)