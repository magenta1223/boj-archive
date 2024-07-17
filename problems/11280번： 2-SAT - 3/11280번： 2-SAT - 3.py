#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11280                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11280                         #+#        #+#      #+#     #
#     Solved: 2024-07-17 04:50:03 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# https://justicehui.github.io/hard-algorithm/2019/05/17/2SAT/

# N개의 boolean 변수 x_1 ~ x_n 
# 2-CNF식을 true로 만들기 위해 x_i를 어떻게 바꿔야 하는가? 

# 2-CNF
# (x or y) and (not y or z) and (x or not z)and (z or y)
# 괄호로 묶인 영역을 절 (cluase)라 하고, 각 절은 두 변수의 or연산
# dp네 

# 각 식이 전부 true가 되어야 함. 그렇게 되는 x_i가 존재하나?

# i,j가 양수 -> x_i, x_j
# 음수 -> not x_(-i), not x_(-j)

# SCC인데
# dfs로 탐색 중, 같은 곳에 도달 + 값이 달라야 함 -> 모순 -> 실패 
# 한 경우라도 성공 가능한지 확인 


# x_i or x_j 
# i가 음수면
# not x_(-i) = not x_(N-i)

# 1. 1<=i<=N 
# => -i = N+1-i 

# true, false를 어떻게 정할거지? 
# => 순방향과 역방향 그래프로 정하자 
# true면 순방향, false면 역방향 

# 둘 다 양수 -> 순방향 그래프에 서로 추가
# 둘 다 음수 -> 역방향 그래프에 추가 
# 둘 중 하나만 양수 -> 뭐 맞게 처리 





import sys
from collections import defaultdict

sys.setrecursionlimit(10100)

def notX(x):
    return x ^ 1

def trueX(x):
    return x << 1

def falseX(x):
    return (x << 1) | 1

def dfs(v):
    visit[v] = 1
    for u in G[v]:
        if not visit[u]:
            dfs(u)
    dfn.append(v)

def revdfs(v, color):
    visit[v] = 1
    scc[v] = color
    for u in revG[v]:
        if not visit[u]:
            revdfs(u, color)

input = open(0).readline

N,M = map(int, input().split())

G = defaultdict(list)
revG = defaultdict(list)


# graph의 키는 
# 2~2*N+1까지 존재
# 각각 대응하는 수는
# key    (2, 3), .... 
# i      (1,-1),       (2,-2)
# value  (x_1,x_(-1)) .. 

for _ in range(M):
    i,j = map(int, input().split())
    if i > 0:
        i = trueX(i)
    else:
        i = falseX(-i)
    if j > 0:
        j = trueX(j)
    else:
        j = falseX(-j)

    # x_i or x_j = true여야 함
    # x_i가 false면 x_j는 반드시 true 
    # x_j가 false라면 x_i는 반드시 true 
    
    G[notX(i)].append(j)
    G[notX(j)].append(i)
    revG[j].append(notX(i))
    revG[i].append(notX(j))

dfn = []
scc = [0] * (2 * N + 2)


visit = [0] * (2*N+2)
for i in range(2, N*2+2):
    if not visit[i]:
        dfs(i)

visit = [0] * (2*N+2)
dfn.reverse()
cnt = 1
for i in dfn:
    if not visit[i]:
        revdfs(i, cnt)
        cnt += 1


for i in range(1, N + 1):
    # 하나의 scc안에서 순방향과 역방향이 동시에 방문되는 경우
    # 불가능함. 
    if scc[trueX(i)] == scc[falseX(i)]:
        print(0)
        exit(0)
print(1)
