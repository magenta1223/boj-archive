#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1315                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1315                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 15:06:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MAX = 1000 + 1
def clear(_str, _int):
    global Q 
    pnts = [q[2] for q in Q if _str >= q[0] or _int >= q[1]]
    return sum(pnts), len(pnts) 
 
N = int(input())
Q = [list(map(int,input().split())) for _ in range(N)]
 
dp = [[-1] * MAX  for _ in range(MAX)]
 
def dfs(_str, _int, prev_pnts, prev_cleared):
    if dp[_str][_int] != -1:
        return dp[_str][_int]
    # 1. 가능한 quest 깨기 
    pnts, cleared = clear(_str, _int)
    dp[_str][_int] = cleared 
 
    if prev_cleared == cleared: # 깬 개수가 똑같으면 -> 더 이상 깰 수가 없음. 
        return dp[_str][_int]
    
    # 2. 남은 포인트 분배 
    left_pnts = pnts-prev_pnts
    for s in range(left_pnts+1):
        next_s, next_i = min(_str+s, 1000), min(_int+left_pnts-s, 1000)
        dp[_str][_int] = max(dp[_str][_int], dfs(next_s, next_i, pnts, cleared))
    return dp[_str][_int]
 
print(dfs(1,1,0,0))