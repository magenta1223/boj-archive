#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2613                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2613                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 03:22:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# INF = float("inf")
# N,M = map(int,input().split())
# A = list(map(int,input().split()))

# # N개의 수로 구성된 A를 M개의 그룹으로 나눈다
# # 각 그룹의 합의 최댓값의 최댓값이 가장 작아지도록 만들고
# # 그 최댓값을 만드는 그룹을 찾으면 됨 
# # dfs로 


INF = float("inf")
N,M = map(int,input().split())
A = list(map(int,input().split()))

S = [0] * N 
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1] + A[i]
def partsum(a,b):
    return S[b-1] - (S[a-1] if a>0 else 0)


dp = [[0] * M for _ in range(N)]
backtrack = [[-1] * M for _ in range(N)]

def dfs(idx, nInterval):
    if nInterval == M-1:
        dp[idx][nInterval] = partsum(idx, N)
        backtrack[idx][nInterval] = N 
        return dp[idx][nInterval]

    if dp[idx][nInterval]:
        return dp[idx][nInterval]

    res =  INF
    resIdx = -1
    for next in range(idx+1, N-M+nInterval+2):
        _res = max(partsum(idx, next), dfs(next, nInterval+1))        
        if res > _res:
            res = _res 
            resIdx = next 
    
    dp[idx][nInterval] = res     
    backtrack[idx][nInterval] = resIdx 
    return dp[idx][nInterval]

ans = dfs(0,0)
paths = []
start = 0 
for i in range(M):
    paths.append(backtrack[start][i]-start)
    start = backtrack[start][i] 

print(ans)
print(*paths)

