#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2133                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2133                          #+#        #+#      #+#     #
#     Solved: 2024-03-12 23:27:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
if N%2:
    print(0)
else:
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    dp[2] = 3
    for i in range(3, N+1):
        # 짝수만 
        if i % 2:
            continue
        for k in range(1,i+2):
            if k % 2:
                continue
            dp[i] += dp[i-k] * 2 
        dp[i] += dp[i-2]
    print(dp[-1])