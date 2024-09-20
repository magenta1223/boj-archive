#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13306                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13306                         #+#        #+#      #+#     #
#     Solved: 2024-09-20 07:17:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 1. N-1번 엣지를 끊고
# 2. Q번 연결 여부를 확인 
# -> 연결 여부를 unf로 확인하고, N-1번 잇는걸로 바꾸기 

import sys 
sys.setrecursionlimit(200_010)
input = open(0).readline 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]

N,Q = map(int, input().split())
parent = [i for i in range(N+1)]
GT = [0] * (N+1)
for i in range(1,N):
    GT[i+1] = int(input())

inps = [list(map(int, input().split())) for _ in range(N+Q-1)]
ans = [''] * Q 
q = Q-1 

for inp in inps[::-1]:
    if inp[0]:
        # c,d가 연결 되어있는가?  
        _,c,d = inp 
        ans[q] = 'YES' if find(c) == find(d) else 'NO'
        q -= 1 
    else:
        # b의 부모정점과의 엣지를 끊기  
        _,b = inp 
        parent[b] = GT[b]

print(*ans, sep = '\n')
