#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1976                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1976                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 15:52:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
M = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
P = list(map(int,input().split()))
P = [p-1 for p in P]
 
# 각 도시가 연결 되었는지 아닌지 ? 
# 연결된 두 도시에 대해 union 과정을 수행
# 그리고 P에서 조회를 슥 했을 때 안되면 -> 너 나가! 
 
parents = [i for i in range(N)]
 
def find(a):
    if a == parents[a]:
        return a 
    parents[a] = find(parents[a])
    return parents[a]
 
def union(a, b):
    a, b = find(a), find(b)
    a, b = (a, b) if a < b else (b, a)
    parents[a] = b 
    
for i in range(N):
    for j in range(N):
        if W[i][j]:
            union(i,j)
                        
for i in range(len(P)-1):
    if find(P[i]) != find(P[i+1]):
        print("NO")
        exit(0)
print("YES")