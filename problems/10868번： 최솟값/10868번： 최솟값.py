#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10868                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10868                         #+#        #+#      #+#     #
#     Solved: 2024-05-16 11:39:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil, log2 
 
input = open(0).readline
 
INF = float("inf")
 
N,M = map(int,input().split())
A = [int(input()) for _ in range(N)]
 
TREE = [0] * (1 << (ceil(log2(N))+1) )
 
def init(idx, s, e):
    if s == e:
        TREE[idx] = A[s]
        return TREE[idx]
    mid = (s+e) // 2 
    l, r = init(idx*2,s, mid), init(idx*2+1, mid+1, e)
    TREE[idx] = min(l,r)
    return TREE[idx]
 
def get(idx, s, e):
    if s > b or e < a:
        return INF    
    if a <= s and e <= b:
        return TREE[idx]
    else:
        mid = (s+e)//2 
        l,r = get(idx*2, s, mid), get(idx*2+1, mid+1, e)
        return min(l,r)
 
init(1, 0, N-1)
 
for _ in range(M):
    a,b = map(int,input().split())
    a, b = a-1, b-1
    print(get(1,0,N-1))