#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2618                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2618                          #+#        #+#      #+#     #
#     Solved: 2024-02-07 11:14:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
W=int(input().strip())
COORDS = [list(map(int, input().split())) for _ in range(W)]
COORDS = [[[1,1]] + COORDS, [[N,N]] + COORDS]
 
# DP Table : i,j = 차1이 i번째 사건을 마지막으로 처리, 차2가 j번째 사건을 마지막으로 처리 
# 이때 최소 이동거리 
# dp table은 사건 순으로 업데이트 
dp = [[float('inf')] * (W+1)  for _ in range(W+1)]
history = [[[-1, -1, -1]] * (W+1) for _ in range(W+1)]
 
 
dp[0][0] = 0
 
def getDist(car_index, c1, c2):
    c1 = COORDS[car_index][c1]
    c2 = COORDS[car_index][c2]
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
 
for w in range(1,W+1):
    coords = COORDS[0][w]
    # w번째 사건을 추가할 수 있는 dp_table의 index는?
    # 둘 중 하나가 w-1인 케이스임. 
    # 즉, dp[x][w-1] or dp[w-1][x] x는 0~w-2
    # w번째 사건을 0으로 풀수도, 1로 풀수도 있음. 
    
    for i in range(w):    
        d = getDist(0,i,w)
        if dp[i][w-1] + d < dp[w][w-1]:
            dp[w][w-1] =  dp[i][w-1] + d
            history[w][w - 1] = [i, w - 1, 1]
        
        # 1번차로 해결 
        d = getDist(1,w-1, w)
        if dp[i][w-1] + d < dp[i][w]:
            dp[i][w] =  dp[i][w-1] + d
            history[i][w] = [i, w-1, 2]
 
        # dp[w-1][i]
        # 0번차로 해결 
        d = getDist(0,w-1, w)
        if dp[w-1][i] + d < dp[w][i]:
            dp[w][i] = dp[w-1][i] + d
            history[w][i] = [w-1, i, 1]
        # 1번차로 해결 -> 1번차의 현재 위치 
        d = getDist(1,i, w)
        if dp[w-1][i] + d < dp[w-1][w]:
            dp[w-1][w]= dp[w-1][i] + d
            history[w - 1][w] = [w-1, i, 2]
 
 
 
min_dist = float('inf')
last_event = 0
car_chosen = 0
for i in range(W+1):
    if dp[i][W] < min_dist:
        min_dist = dp[i][W]
        x,y = i, W
        car = 2
    if dp[W][i] < min_dist:
        min_dist = dp[W][i]
        x,y = W,i
        car = 1
 
 
# 역추적하여 경로 복원
path = []
while car != -1:
    path.append(car) 
    x, y, car = history[x][y]
path.reverse() 
print(min_dist)
print(*path[:-1], sep='\n')