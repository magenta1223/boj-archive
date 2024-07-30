#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2637                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2637                          #+#        #+#      #+#     #
#     Solved: 2024-07-30 01:59:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 사이클은 없다 = 유향 비순환 그래프 

from collections import defaultdict

N = int(input())
M = int(input())
G = {i: [] for i in range(1,N+1)}
for _ in range(M):
    x,y,k = map(int, input().split())
    G[x].append((y,k))


# dfs + dp with recurrent func 
dp = {i : None for i in range(1,N+1)}
def dfs(idx)->dict:
    if dp[idx] is not None:
        return dp[idx]
    if not G[idx]:
        dp[idx] = {idx:1}
        return dp[idx]
    res = defaultdict(int)
    for part, cnt in G[idx]:
        partDict = dfs(part)
        for k, v in partDict.items():
            res[k] += v*cnt 
    dp[idx] = res 
    return dp[idx]
ans = dfs(N)
for k in sorted(ans.keys()):
    print(k, ans[k])



# # dfs+dp w/o reccurent func 
# # stack 

# stack = [N]
# visited = [False] * (N+1)
# dp = {i : None for i in range(1,N+1)}

# while stack:
#     if visited[stack[-1]]:
#         if dp[stack[-1]] is not None:
#             stack.pop()
#             continue
#         else:
#             d, idx = defaultdict(int), stack.pop()
#             if G[idx]:
#                 for sub, cnt in G[idx]:
#                     for k, v in dp[sub].items():
#                         d[k] += v*cnt 
#             else:
#                 d = {idx:1} 
#             dp[idx] = d 
#     else:
#         visited[stack[-1]] = True 
#         for sub, cnt in G[stack[-1]]:
#             stack.append(sub)

# for k in sorted(dp[N].keys()):
#     print(k, dp[N][k])
