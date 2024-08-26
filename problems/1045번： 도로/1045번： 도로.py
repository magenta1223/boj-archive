#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1045                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1045                          #+#        #+#      #+#     #
#     Solved: 2024-08-26 03:01:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from heapq import heappop, heappush 

D = {'Y':1, 'N':0}
def T(x):
    return D[x]

N,M = map(int, input().split())
ADJ = [list(map(T, list(input()))) for _ in range(N)]
ROADS = []
for i in range(N):
    for j in range(i+1,N):
        if ADJ[i][j]:
            heappush(ROADS, (i,j))

def solution():
    def find(a):
        if a == parent[a]:
            return a 
        parent[a] = find(parent[a])
        return parent[a]

    if len(ROADS) < M:
        return -1 

    parent = [i for i in range(N)]
    ans = [0] * N 
    remains = []
    visited = 0 

    while ROADS:
        a,b = heappop(ROADS)
        pa,pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb 
            ans[a] += 1
            ans[b] += 1 
            visited += 1 
        else:
            heappush(remains, (a,b))

    if visited != N-1:
        return -1 

    lefts = M-visited # visited = N-1 
    while lefts:
        a,b = heappop(remains)
        ans[a] += 1 
        ans[b] += 1 
        lefts -= 1

    return ans 

ans = solution()
if ans != -1:
    print(*ans)
else:
    print(ans)


"""
4 3
NYYN
YNYN
YYNY
NNYN

"""