#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1167                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1167                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 12:57:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
V = int(input())
G = {i : [] for i in range(1,V+1)}
for _ in range(V):
    adjs = list(map(int,input().split()))
    a, adjs = adjs[0], adjs[1:]
    for i in range(len(adjs) //2):
        G[a].append(tuple(adjs[i*2:i*2+2]))
 
ans = 0
def dfs(node, pnode, cost):
    global ans 
    if not sum([1 for cnode, _ in G[node] if cnode != pnode]):
        ans = max(ans, cost)
        return cost 
    children = []
    for cnode, c in G[node]:
        if cnode == pnode:
            continue
        # 누적비용 - 현재비용 
        children.append(dfs(cnode, node, cost + c) - cost)            
    
    costs = [cost] + children
    costs.sort()
    ans = max(ans, sum(costs[-2:]))
    
    return max(children) + cost 
 
# 1. 루트를 정하고 내려감
# 2. leaf라면 -> 누적비용과 ans를 비교 
# 3. leaf가 아니라면 -> child를 끝까지 내렸을 때의 누적비용 - 현재 비용 을 모든 children에 대해 계산
# 3-1) 누적비용과 조합 최대비용을 계산 
 
dfs(1,0,0)
 
print(ans)