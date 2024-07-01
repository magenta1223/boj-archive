#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1029                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1029                          #+#        #+#      #+#     #
#     Solved: 2024-05-24 14:02:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
P = [list(map(int, list(input()))) for _ in range(N)]
# P[i][j]: 그림이 i번사람->j번 사람으로 갈 때의 가격
dp = [[[-1] * 10 for _ in range(N)] for _ in range(1<<N)] 
max_prices = [max(l) for l in P]
FULL = (1<<N) -1
 
 
def dfs(bitmask, artist, price, n):
    # prefix = "--" *n
    # ? 
    if dp[bitmask][artist][price] != -1:
        # print(prefix, "이미 계산함")
        return dp[bitmask][artist][price]
 
    if price > max_prices[artist] or bitmask == FULL:
        # print(prefix+f"{artist}는 팔 수 없음")
        dp[bitmask][artist][price] = n
        return n 
 
    # 다음 사람에게 판다
    res = n # 
    for i in range(N):
        if (1<<i) & bitmask or P[artist][i] < price:
            # 이미 구매한 적이 있음 or 판매 불가  
            continue 
        # 새로 구매 
        # print(prefix+f"{artist}->{i}, {P[artist][i]}원에 판매")
        res = max(res, dfs(bitmask|(1<<i), i, P[artist][i], n+1))
    dp[bitmask][artist][price] = res 
    return dp[bitmask][artist][price]
    
 
print(dfs(1,0,0,1))
 