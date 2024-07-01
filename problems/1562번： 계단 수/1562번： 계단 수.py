#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1562                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1562                          #+#        #+#      #+#     #
#     Solved: 2024-03-15 22:38:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
# 남은 자릿수, 0~9 사용 여부 bitmasking, 마지막 숫자 
dp = [[[-1] * 10 for _ in range(1<<10)] for _ in range(N)]
ADJS = {0:[1], 9:[8]}
for i in range(1,9):
    ADJS[i] = [i-1,i+1]
ADJS[-1] = list(range(1,10))
FULL = (1<<10) - 1
 
def dfs(depth, bitmask, end_num):
    # n자리 
    if depth == N:
        return 1 if bitmask == FULL else 0
    
    if dp[depth][bitmask][end_num] != -1:
        return dp[depth][bitmask][end_num]
    dp[depth][bitmask][end_num] = 0  
    if bitmask == FULL:
        for next_endnum in ADJS[end_num]:
            dp[depth][bitmask][end_num] += dfs(depth+1, bitmask, next_endnum) 
    else:
        for next_endnum in ADJS[end_num]:
            dp[depth][bitmask][end_num] += dfs(depth+1, bitmask | (1<<next_endnum), next_endnum) 
 
    return dp[depth][bitmask][end_num] % 1_000_000_000
 
print(dfs(0,0,-1))