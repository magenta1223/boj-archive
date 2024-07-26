#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13308                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13308                         #+#        #+#      #+#     #
#     Solved: 2024-07-25 01:15:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from heapq import heappop, heappush 

INF = float("inf")
input = open(0).readline 

N,M = map(int,input().split())
P = [-1]+list(map(int,input().split()))
G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))

def dijkstra():
    inf = float("inf")
    # dp[i][j] : i번 도시에 주유비용 j로 도달하는 최소 비용 
    dp = [[inf] * (max(P) + 1) for _ in range(N + 1)]
    q = []
    dp[1][P[1]] = 0
    heappush(q, (0, P[1], 1))
    while q:
        curCost, curPrice, now = heappop(q)
        # 도착 시 정답 리턴
        if now == N:
            return curCost
        
        if dp[now][curPrice] < curCost:
            continue

        for next, d in G[now]:
            nextPrice = min(P[next], curPrice)
            nextCost = curCost + curPrice * d
            if dp[next][curPrice] > nextCost:
                dp[next][curPrice] = nextCost
                heappush(q, (nextCost, nextPrice, next))

print(dijkstra())