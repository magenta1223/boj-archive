#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20040                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20040                         #+#        #+#      #+#     #
#     Solved: 2024-04-11 14:42:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
 
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    a, b = find(a), find(b)
    if a!=b:
        if a > b:
            parent[a] = parent[b]
        else:
            parent[b] = parent[a]
    else:
        # cycle 
        print(i+1)
        exit(0)
print(0)