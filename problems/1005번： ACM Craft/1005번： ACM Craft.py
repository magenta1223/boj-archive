#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1005                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1005                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 10:38:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque  
def solve(parents, build_times, target):
    visited = [-1] * (N+1)  
    visited[target] = build_times[target-1]  
    queue = deque([target])
    roots = set()
    
    while queue:
        node = queue.popleft()
        # 부모 노드 
        if parents[node]:
            for pnode in parents[node]:
                # 현재 노드 도착비용 + 부모노드 포함비용 
                cost = visited[node] + build_times[pnode-1]
                if visited[pnode] < cost:
                    visited[pnode] = cost
                    queue.append(pnode)
        else:
            roots.add(node)
    ans = [visited[root] for root in roots]
 
    return max(ans) 
 
T=int(input())
for _ in range(T):
    N,K = map(int,input().split())
    BUILD_TIMES = list(map(int,input().split()))
    parents  = {i : [] for i in range(1,N+1)}
    for _ in range(K):
        a,b = map(int,input().split())
        parents[b].append(a)
 
    W = int(input())
    print(solve(parents,BUILD_TIMES, W))