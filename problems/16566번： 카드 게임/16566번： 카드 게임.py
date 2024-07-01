#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16566                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16566                         #+#        #+#      #+#     #
#     Solved: 2024-04-11 19:22:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from bisect import bisect_right
 
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]
 
def union(a, b):
    if b >= M:
        return
    # b가 a보다 반드시 큼 
    a,b = find(a), find(b)
    if a != b:
        parent[a] = b # a를 사용 못하면 그거보다 큰걸 사용해야 함. 
 
N,M,K = map(int,input().split())
Card = sorted(list(map(int,input().split())))
parent = [i for i in range(M)]
for num in map(int,input().split()):
    idx = find(bisect_right(Card, num))
    print(Card[idx])
    union(idx, idx+1)