#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2618                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2618                          #+#        #+#      #+#     #
#     Solved: 2024-07-22 07:54:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
INF = float("inf")

def getDist(car,a,b):
    x1,y1 = CASES[car][a]
    x2,y2 = CASES[car][b]
    return abs(x2-x1) + abs(y2-y1)


N,W = int(input()), int(input())
dp = [[INF] * (W+1) for _ in range(W+1)]
backtrack = [[-1] * (W+1) for _ in range(W+1)]

CASES = [list(map(int,input().split())) for _ in range(W)]
CASES = [[[1,1]] + CASES, [[N,N]] + CASES]


dp[0][0] = 0 
dp[1][0] = getDist(0,0,1)
dp[0][1] =  getDist(1,0,1)

for i in range(1,W+1):
    for j in range(i-1):
        # 경찰차 1이 i를 처리 
        # 직전사건을 경찰차 1이 처리
        if dp[i][j] > dp[i-1][j] + getDist(0,i-1,i):
            dp[i][j] = dp[i-1][j] + getDist(0,i-1,i)
            backtrack[i][j] = (i-1,j)

        
        # 직전사건을 경찰차2가 처리 
        if dp[i][i-1] > dp[j][i-1] + getDist(0,j,i):
            dp[i][i-1] = dp[j][i-1] + getDist(0,j,i)
            backtrack[i][i-1] = (j,i-1)

        # 경찰차 2가 i를 처리 
        # 직전사건을 경찰차 1이 처리
        if dp[i-1][i] > dp[i-1][j] + getDist(1,j,i):
            dp[i-1][i] = dp[i-1][j] + getDist(1,j,i)
            backtrack[i-1][i] = (i-1,j)

        # 직전사건을 경찰차2가 처리 
        if dp[j][i] > dp[j][i-1] + getDist(1,i-1,i):
            dp[j][i] = dp[j][i-1] + getDist(1,i-1,i)
            backtrack[j][i] = (j,i-1)
    
ans = INF 
for i in range(W):
    if ans > dp[W][i]:
        ans = dp[W][i]
        a,b = W,i 
    if ans > dp[i][W]:
        ans = dp[i][W]
        a,b = i,W

cars = [1 if a>b else 2]
while backtrack[a][b] != -1:
    a,b = backtrack[a][b]
    cars.append(1 if a>b else 2)

print(ans)
print(*cars[::-1], sep ='\n')
