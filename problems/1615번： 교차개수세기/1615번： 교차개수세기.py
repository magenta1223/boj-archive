#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1615                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1615                          #+#        #+#      #+#     #
#     Solved: 2024-09-19 00:38:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 간선의 교차 갯수를 출력 
# 1. 시점,종점 순으로 정렬 
# 2. 간선을 하나씩 추가한다. 
# 이 때, 시점은 반드시 같거나 크므로 고려할 필요가 없고, 종점을 기준으로 교차여부를 판단하면 됨. 
# 교차 = 시점이 크고 종점이 작거나, 시점이 작고 종점이 크거나
# 전자의 경우는 존재 x
# 즉, 현재 종점보다 큰 것의 카운트를 세면 된다. 

class FenwickTree:
    def __init__(self, n):
        self.n = n 
        self.tree = [0] * (n+1)
    def update(self, x, delta):
        while x <= self.n:
            self.tree[x] += delta 
            x += x&-x 
    def query(self, x):
        res = 0 
        while x>0:
            res += self.tree[x]
            x -= x&-x 
        return res 

    def rangeQuery(self, a, b):
        return self.query(b) - self.query(a-1) 

input = open(0).readline 
N,M = map(int,input().split())

# 최대 2백만개라 sort하면 메모리 초과? 
# E = [list(map(int,input().split())) for _ in range(M)]
# E.sort(key = lambda x:(x[0], x[1]))
# ans = 0
# fwtree = FenwickTree(N)
# for a,b in E:
#     ans += fwtree.rangeQuery(b+1, N)
#     fwtree.update(b,1)

# print(ans)


from collections import defaultdict 
E = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split()) 
    E[a].append(b)

ans = 0
fwtree = FenwickTree(N)
for s in range(1,N+1):
    E[s].sort()
    for b in E[s]:
        ans += fwtree.rangeQuery(b+1, N)
        fwtree.update(b,1)

print(ans)