#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9372                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9372                          #+#        #+#      #+#     #
#     Solved: 2024-06-12 15:22:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
def find(a):
    if a==parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
for _ in range(int(input())):
    N,M = map(int,input().split())
    parent = [i for i in range(N+1)]
    ans = 0
    for i in range(M):
        a,b = map(int,input().split()) 
        a,b = find(a), find(b)
        if a!=b:
            parent[a] = b 
            ans += 1 
    print(ans)