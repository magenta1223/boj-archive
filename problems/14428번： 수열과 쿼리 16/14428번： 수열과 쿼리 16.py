#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14428                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14428                         #+#        #+#      #+#     #
#     Solved: 2024-05-22 13:17:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil, log2
 
 
 
INF = float("inf")
 
def init(idx, s, e):
    if s == e:
        TREE[idx] = A[s], s
        return TREE[idx]
    
    mid = (s+e)//2 
    l,l_idx = init(idx*2, s,mid)
    r,r_idx = init(idx*2+1, mid+1, e)
    TREE[idx] = (l, l_idx) if l <= r else (r, r_idx)
    return TREE[idx] 
 
def update(idx, s, e):
    # 범위 바깥인지 
    if not s <= target <= e:
        return TREE[idx]
    # 딱 거기인지 
    if s == e:
        A[s] = value 
        TREE[idx] = value, s
        return TREE[idx]
    
    mid = (s+e)//2 
    l,l_idx = update(idx*2, s,mid)
    r,r_idx = update(idx*2+1, mid+1, e)
    TREE[idx] = (l, l_idx) if l <= r else (r, r_idx)
    return TREE[idx] 
 
def get(idx, s, e):
 
    if e < frm or to < s:
        return INF, -1
    
    if frm <= s and e <= to:
        return TREE[idx]
 
    mid = (s+e)//2
 
    l,l_idx = get(idx*2, s, mid)
    r,r_idx = get(idx*2+1, mid+1, e)
 
    return (l, l_idx) if l<=r else (r, r_idx)
 
 
input = open(0).readline 
N = int(input())
A = list(map(int,input().split()))
M = int(input())
 
TREE = [0] * (1<<(ceil(log2(N))+1))
 
 
 
init(1,0,N-1)
 
for _ in range(M):
    query,a,b = map(int,input().split())
    
    if query == 1:
        target, value = a-1, b
        update(1,0,N-1)
    else:
        frm, to = a-1, b-1 
        print(get(1,0,N-1)[-1]+1)