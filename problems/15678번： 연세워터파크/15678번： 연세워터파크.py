#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15678                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15678                         #+#        #+#      #+#     #
#     Solved: 2024-06-04 15:11:03 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,D = map(int,input().split())
K = list(map(int,input().split()))
 
 
 
INF = float("inf")
dp = [-INF] * N 
 
dp[0] = K[0]
 
from math import ceil, log2 
TREE = [0] * (1<<(ceil(log2(N))+1))
 
def init(idx,s,e):
    if s==e:
        TREE[idx] = dp[s]
        return TREE[idx]
    mid = (s+e)//2
    l = init(idx*2,s,mid)
    r = init(idx*2+1,mid+1, e)
    TREE[idx] = max(l,r)
    return TREE[idx]
 
def update(idx,s,e):
    # 범위 바깥인지?
    if not s<= i <=e:
        return TREE[idx] 
     
    if s==e:
        TREE[idx] = v 
        return TREE[idx]
    
    mid = (s+e)//2
    l = update(idx*2,s,mid)
    r = update(idx*2+1,mid+1, e)
    TREE[idx] = max(l,r)
    return TREE[idx]
 
def get(idx,s,e):
    if e < frm or to < s:
        return -INF 
    if frm <= s and e <=to:
        return TREE[idx]
    mid = (s+e)//2
    l = get(idx*2,s,mid)
    r = get(idx*2+1,mid+1, e)
    return max(l,r)
 
 
init(1,0,N-1)
 
for i in range(1,N):
    frm, to = max(0,i-D), i-1 
    dp_se = get(1,0,N-1)
    dp[i] = max(K[i], dp_se+K[i])
    v = dp[i]
    update(1,0,N-1)
    # dp[i] = max(K[i], max(dp[max(0,i-D):i]) + K[i])
print(max(dp))