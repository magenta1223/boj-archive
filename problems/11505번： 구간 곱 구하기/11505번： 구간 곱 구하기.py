#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11505                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11505                         #+#        #+#      #+#     #
#     Solved: 2024-04-24 17:39:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math
input = open(0).readline
MOD = 1_000_000_007
 
N,M,K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
 
b = math.ceil(math.log2(N)) + 1
node_n = 1 << b
TREE = [0 for _ in range(node_n)]
 
 
def init(idx, s, e):
    if s == e:
        TREE[idx] = arr[s]
        return TREE[idx]
    mid = (s+e) // 2
    # left subtree는 현재 index에 2배, right는 그 다음. 
    # 이진트리 -> 2배가 됨. index구성의 용이함때문에 첫 index가 1에서 시작 
    l = init(idx*2, s, mid)
    r = init(idx*2+1, mid+1, e)
    TREE[idx] = (l*r) % MOD
    return TREE[idx]
 
 
def update(idx, s, e):
    if not s <= b-1 <= e:  # 범위 밖
        return TREE[idx]
    if s == e:
        TREE[idx] = new
        return new
    mid = (s+e) // 2
    l = update(idx*2, s, mid)
    r = update(idx*2+1, mid+1, e)
    TREE[idx] = (l*r) % MOD
    return TREE[idx]
 
 
def get(idx, s, e):
    # 탐색 영역 : s~e
    if to<s or e<frm:  # 범위 밖
        return 1 # 곱셈의 항등원 
 
    mid = (s+e)//2
    if frm <= s and e <= to:  # 값을 구하려는 범위가 현재 subtree의 범위와 정확히 겹침 
        return TREE[idx]
 
    else:  # 정확히 겹치지 않음 
        l = get(idx*2, s, mid)
        r = get(idx*2+1, mid+1, e)
        return (l*r) % MOD
 
init(1, 0, N-1)
 
 
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        cur, new = arr[b-1], c
        update(1, 0, N-1)
    else:
        frm, to = b-1, c-1
        print(get(1, 0, N-1) % MOD)