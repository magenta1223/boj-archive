#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1275                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1275                          #+#        #+#      #+#     #
#     Solved: 2024-07-30 01:39:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


input = open(0).readline 

N,Q = map(int, input().split())
A = list(map(int, input().split()))

# -------------------------------------------- #  
from math import ceil, log2 

TREE = [0 for _ in range(1<<(ceil(log2(N))+1))]

def init(idx, s, e):
    if s==e:
        TREE[idx] = A[s]
        return TREE[idx]
    mid = (s+e)//2 
    TREE[idx] = init(idx*2, s, mid) + init(idx*2+1, mid+1, e)
    return TREE[idx]

def get(idx, s, e):
    if to < s or e < frm:
        return 0 
    
    if frm<=s and e<=to:
        return TREE[idx]
    mid = (s+e)//2 
    return get(idx*2, s, mid) + get(idx*2+1, mid+1, e)

def update(idx, s, e):
    if not s<=a<=e:
        return TREE[idx]
    if s==e:
        A[s] = b 
        TREE[idx] = b 
        return TREE[idx]
    mid = (s+e)//2 
    TREE[idx] = update(idx*2, s, mid) + update(idx*2+1, mid+1, e)
    return TREE[idx]

init(1,0,N-1)
for _ in range(Q):
    frm,to,a,b = map(int, input().split())
    frm, to, a = frm-1, to-1, a-1
    frm, to = sorted([frm, to])
    
    print(get(1, 0, N-1))
    update(1, 0, N-1)
    

"""
5 6
1 2 3 4 5
2 3 3 1
3 5 4 1
2 3 3 1
3 5 4 1
3 4 3 11
3 4 2 5



"""


# input = open(0).readline 

# N,Q = map(int, input().split())
# A = list(map(int, input().split()))

# # -------------------------------------------- #  




# # -------------------------------------------- # 

# for _ in range(Q):
#     x,y,a,b = map(int, input().split())