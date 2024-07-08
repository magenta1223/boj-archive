#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1135                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1135                          #+#        #+#      #+#     #
#     Solved: 2024-07-08 01:56:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 트리 

# 직속부하한테 전화 거는데 1분
# root에서 시작해서 모든 노드가 전화받는데 걸리는 최소 시간은? 
# 핵심은 전화를 동시에 걸 수 없다는 점. 

# 1. bottom-up으로 진행
# 2. 현재 node의 children nodes에 대해서는 최소시간이 이미 나와있다고 가정 
# 3. 현재 node의 시간은 children nodes의 시간을 기준, 내림차순 정렬해서 걸리는 시간을 전부 재고, 그 최댓값임 

from collections import deque 

N = int(input())
BOSS = list(map(int,input().split()))

# children 
C = {i :[] for i in range(N)}
P = {i :-1 for i in range(N)}

for i, boss in enumerate(BOSS):
    if boss != -1:
        C[boss].append(i) 
        P[i] = boss 

q = deque([])
T = [-1] * N

for i in range(N):
    if not C[i]:
        q.append((i, 0))
        T[i] = 0 

while q:
    node, t = q.popleft()
    boss = P[node]
    if boss!=-1 and all([T[child] != -1 for child in C[boss]]):
        ts = [T[child] for child in C[boss]]
        ts.sort(reverse= True)
        T[boss] = max([t+i for i, t in enumerate(ts, 1)])
        q.append((boss, T[boss]))
print(T[0])
            
            