#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24480                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24480                         #+#        #+#      #+#     #
#     Solved: 2024-01-02 12:10:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0,"rb").readline
N,M,R=map(int, input().split())
graph = {i : [] for i in range(N+1)}
visited=[0 for _ in range(N+1)]
order = 1
for _ in range(M):
    u, v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
# stack 
stack = [R]
visited[R] = order
for k, adj in graph.items():
    adj.sort()
 
# 역순으로 방문
while stack:
    v=stack[-1]
    # 더 이상 방문할게 없다면 패스
    if not graph[v]:
        stack.pop()
        continue # next loop
    else:
        # 방문한 적 없다면 해야겠지?
        u = graph[v].pop()
        if not visited[u]:
            # 방문
            order += 1
            visited[u] = order 
            stack.append(u)
print(*visited[1:], sep="\n")