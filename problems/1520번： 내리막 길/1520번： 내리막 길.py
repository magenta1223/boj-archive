#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1520                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1520                          #+#        #+#      #+#     #
#     Solved: 2023-12-27 16:35:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0, "rb").readline
M,N=map(int, input().split())
array = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
 
def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 
    c = 0
    for _x, _y in [(-1,0), (1,0), (0,-1),(0,1)]:
        new_x, new_y = x+_x, y+_y
        if 0<=new_x<M and 0<=new_y<N:
            # 내려갈 수 있는지? 
            if array[new_x][new_y] < array[x][y]:
                c += dfs(new_x,new_y)
    dp[x][y] = c
    return c 
 
print(dfs(0,0))