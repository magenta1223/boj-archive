#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2042                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2042                          #+#        #+#      #+#     #
#     Solved: 2024-04-24 17:42:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math
input = open(0).readline
 
def init(idx, s, e):
    if s == e:
        TREE[idx] = arr[s]
        return TREE[idx] 
    mid = (s+e)//2
    l = init(idx*2, s, mid)
    r = init(idx*2+1, mid+1, e)
    TREE[idx] = l+r 
    return TREE[idx]
 
def update(idx, s,e):
    if not s <= b-1 <= e: # 갱신 범위 바깥 
        return TREE[idx]
    if s == e:
        TREE[idx] = new
        arr[s] = new 
        return TREE[idx]
    mid = (s+e)//2 
    l = update(idx*2, s, mid)
    r = update(idx*2+1, mid+1, e)
    TREE[idx] = l+r 
    return TREE[idx]
 
def query(idx, s, e):
    # 범위 바깥인가? 
    if to<s or e<frm:  # 범위 밖
        return 0 
    # 완벽히 겹치는가?
    if frm <= s and e <= to:
        return TREE[idx]
    else:
        mid = (s+e)//2 
        l = query(idx*2, s, mid)
        r = query(idx*2+1, mid+1, e)
        return l+r 
 
 
 
N,M,K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
 
node_n = 1 << (math.ceil(math.log2(N)) + 1)
TREE = [0 for _ in range(node_n)]
 
 
init(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        cur, new = arr[b-1], c
        update(1, 0, N-1)
    else:
        frm, to = b-1, c-1
        print(query(1, 0, N-1))
 