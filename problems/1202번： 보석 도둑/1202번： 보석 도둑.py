#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1202                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1202                          #+#        #+#      #+#     #
#     Solved: 2024-04-11 19:37:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from bisect import bisect_right, bisect_left
 
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a, b):
    if b >= K:
        return
    # b가 a보다 반드시 큼 
    a,b = find(a), find(b)
    if a != b:
        parent[a] = b # a를 사용 못하면 그거보다 큰걸 사용해야 함. 
 
N, K = map(int, input().split())
Jewels = [list(map(int, input().split())) for _ in range(N)]
Bags = [int(input()) for _ in range(K)]
Jewels.sort(key=lambda x: x[1], reverse= True)
Bags.sort()
 
parent = [i for i in range(K)]
ans = 0 
used = [False] * K
 
for m, v in Jewels:
    idx = bisect_left(Bags, m)
    if idx < K:
        idx = find(idx)
        if not used[idx]:
            used[idx] = True 
            union(idx, idx+1)
            ans += v 
print(ans)
 