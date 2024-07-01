#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11047                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11047                         #+#        #+#      #+#     #
#     Solved: 2023-12-21 14:32:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,K=map(int, input().split())
coins = [0] * N
for i in range(N):
    coins[i] = int(input())
    if coins[i] <= K:
        idx = i
ans = 0
for i in range(idx, -1, -1):
    n_coin = K//coins[i]
    ans += n_coin
    K -= n_coin * coins[i]
print(ans)