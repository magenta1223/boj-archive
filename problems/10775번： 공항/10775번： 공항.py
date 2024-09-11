#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10775                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10775                         #+#        #+#      #+#     #
#     Solved: 2024-09-11 03:49:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 게이트 G개에 P개의 비행기가 도착 
# 도착 불가능한 순간 공항 폐쇄
# 최대 몇대 도착 가능? 


input = open(0).readline 
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]


G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
Gi = [int(input()) for _ in range(P)]
Gates = [0] * (G+1)
ans = 0 
for gi in Gi:
    # 최대 1~gi 사이에 주차 가능
    # 최대한 많은 비행기를 주차해야 하므로, 가능한한 뒤쪽에 주차 
    gi = find(gi) 
    if not gi:
        break 
    Gates[gi] += 1
    gim1 = find(gi-1)
    parent[gi] = gim1  
    ans += 1 

print(ans)