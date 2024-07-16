#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20188                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20188                         #+#        #+#      #+#     #
#     Solved: 2024-07-16 02:49:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #




# 1번이 루트 
# i<j인 모든 i,j쌍에 대해 루트의 "다양성"의 합을 구함
# 루트의 다양성 = i에서 j로 갈 때, 정상을 거쳐 가는 서로 다른 간선의 개수

# 어떤 간선을 몇 번 지나는지 생각해보자
# 그 간선 아래의 노드들 (A)
# 아닌 노드들 (B)

# A안의 노드 쌍 -> 무조건 지남 (정상을 거침)
# B안의 노드 쌍 -> 절대 안지남
# A와 B의 노드쌍 -> 무조건 지남 

# 즉, 어떤 간선을 지나는 횟수는 그 간선 아래의 노드 개수로 알 수 있다. 

# 간선 아래 = 루트 기준, 도착점 포함 child의 개수 


# import sys 
# sys.setrecursionlimit(310_000)
# input = open(0).readline 

# N = int(input())

# G = {i:[] for i in range(1,N+1)}

# for _ in range(N-1):
#     a,b = map(int,input().split())
#     G[a].append(b)
#     G[b].append(a)

# dp = [-1] * (N+1)

# ans = 0 
# def dfs(node, parent):
#     global ans 

#     dp[node] = 1

#     for next in G[node]:
#         if next != parent:
#             dp_next = dfs(next, node)
#             print(node, next, (dp_next*(dp_next-1)) // 2  +  (dp_next*(N-dp_next)))

#             ans +=  (dp_next*(dp_next-1)) // 2  +  (dp_next*(N-dp_next))
#             dp[node] += dp_next

#     return dp[node]

# dfs(1,0)
# print(ans)




from collections import deque 

input = open(0).readline 

N = int(input())
G = {i:[] for i in range(1,N+1)}
for i in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

P = [0 for _ in range(N+1)] 
S = [1 for _ in range(N+1)]

stack = [1]
dfsord = []
while stack:
    now = stack.pop()
    dfsord.append(now)
    for next in G[now]:
        if next == P[now]:
            continue
        P[next] = now
        stack.append(next)

while dfsord:
    v = dfsord.pop()
    S[P[v]] += S[v]


ans = 0
All = N * (N-1) // 2
for i in range(2,N+1):
    t = N-S[i] # i아래의 노드를 제외한 모든 노드 
    ans += All - t*(t-1) //2

print(ans)
# [8, 1, 1, 2, 5, 3, 1, 1]