#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1199                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1199                          #+#        #+#      #+#     #
#     Solved: 2024-08-21 07:32:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# TSP 같은 문제
# 1. 모든 점을 방문해야 하고
# 2. 간선은 최대 1회만 사용 가능. 
# 3. 두 점 사이에 여러 간선이 존재. 

input = open(0).readline  
N = int(input())
G = []
ADJ_M = [[0] * N for _ in range(N)]
deg = [0] * N 
for i in range(N):
    tmp = {}
    for j, v in enumerate(list(map(int, input().split()))):
        if v:
            deg[i] += v 
            tmp[j] = 0
            ADJ_M[i][j] = v
    G.append(tmp)

if any([d%2 for d in deg]):
    print(-1)
    exit(0)


path = []
stack = [0]
while stack:
    cur = stack[-1]
    if G[cur]:
        _next = next(iter(G[cur]))
        ADJ_M[_next][cur] -= 1
        ADJ_M[cur][_next] -= 1
        if not ADJ_M[cur][_next]:
            del G[cur][_next]
            del G[_next][cur]
        stack.append(_next)
    else:
        # 더이상 갈 곳이 없음 = 하나의 사이클 완성 
        # 현재 사이클의 직전 노드에서 다시 시작. 
        path.append(stack.pop() + 1)

if any([adj for adj in G]):
    print(-1)
else:
    print(*path)


