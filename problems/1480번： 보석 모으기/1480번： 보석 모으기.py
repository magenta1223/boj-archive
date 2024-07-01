#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1480                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1480                          #+#        #+#      #+#     #
#     Solved: 2024-04-25 14:07:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M, C = map(int, input().split())
L = list(map(int, input().split()))
dp = [[[-1] * (C+1) for _ in range(M)] for _ in range(1 << N)]
FULL = (1<<N)-1
def dfs(bitmask, bag_idx, left) :
    if bitmask == FULL or bag_idx == M:
        return 0
    if dp[bitmask][bag_idx][left] != -1:
        return dp[bitmask][bag_idx][left]
    ret = 0
    for i in range(N): 
        if bitmask & (1<<i) or L[i] > C : 
            continue
        if left >= L[i]:
            ret = max(ret, dfs(bitmask|(1<<i), bag_idx, left-L[i])+1)
        else:
            ret = max(ret, dfs(bitmask, bag_idx + 1, C))
    dp[bitmask][bag_idx][left] = ret
    return dp[bitmask][bag_idx][left]
print(dfs(0, 0, C))