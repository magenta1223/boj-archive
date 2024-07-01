#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11780                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11780                         #+#        #+#      #+#     #
#     Solved: 2024-02-07 15:10:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
M=int(input().strip())
dp = [[float("inf")] * N for _ in range(N)]
hist = [[-1] * N for _ in range(N)]
for _ in range(M):
    d,a,c = map(int,input().split())
    d-=1
    a-=1
    if dp[d][a] > c:
        dp[d][a] = c
for i in range(N):
    dp[i][i] = 0
 
# floyd 
# 라운드 = 중간노드 
for k in range(N):
    for i in range(N):
        for j in range(N):
            # i-> j가 i->k->j보다 싼 경우 
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                hist[i][j] = k
 
for line in dp:
    print(*[ 0 if el == float('inf') else el for el in line])
 
 
def backtrack(hist, dp, i, j):
    if dp[i][j] == float('inf'):  # 경로가 존재하지 않는 경우
        return []
    k = hist[i][j]
    if k == -1:
        return [j+1] if i != j else []  # 자기 자신으로의 경로가 아닌 경우에만 추가
    else:
        return backtrack(hist, dp, i, k) + backtrack(hist, dp, k, j)
 
# 출력 수정
for i in range(N):
    for j in range(N):
        if dp[i][j] in [float('inf'), 0]:  # 경로가 존재하지 않는 경우
            print(0)
        else:
            result = [i+1] + backtrack(hist, dp, i, j)
            if not result:  # 결과 리스트가 비어 있는 경우
                print(0)
            else:
                print(len(result), *result)
 