#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2357                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2357                          #+#        #+#      #+#     #
#     Solved: 2024-04-24 18:53:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil, log2 
input = open(0).readline
 
MIN, MAX = 0, 1_000_000_001
 
def init(i,s,e):
    if s==e:
        MINTREE[i] = L[s]
        MAXTREE[i] = L[s]
        return MINTREE[i], MAXTREE[i]
    mid = (s+e)//2 
    min_l, max_l = init(i*2, s, mid)
    min_r, max_r = init(i*2+1, mid+1, e)
    MINTREE[i] = min(min_l,min_r)
    MAXTREE[i] = max(max_l,max_r)
    return MINTREE[i], MAXTREE[i]
 
def query(i,s,e):
    if to < s or frm > e:
        # 해당 없음 
        return MAX, MIN
    
    if frm <= s and e <= to:
        return MINTREE[i], MAXTREE[i]
 
    mid = (s+e)//2 
    min_l, max_l = query(i*2, s, mid)
    min_r, max_r = query(i*2+1, mid+1, e)
    return min(min_l,min_r), max(max_l,max_r)
 
 
N, M = map(int, input().split())
L = [int(input()) for _ in range(N)]
MINTREE = [0] * (1<<(ceil(log2(N))+1))
MAXTREE = [0] * (1<<(ceil(log2(N))+1))
 
init(1, 0, N-1)
 
for _ in range(M):
    frm, to = map(int, input().split())
    frm, to = frm-1, to-1
    print(*query(1, 0, N-1))
 