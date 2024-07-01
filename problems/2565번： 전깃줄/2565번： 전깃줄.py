#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2565                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2565                          #+#        #+#      #+#     #
#     Solved: 2023-12-20 00:17:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]
l = sorted(l, key=lambda x: x[0])
dp = [1] * N
for i in range(N):
    a,b=l[i]
    for j in range(i):
        _a, _b = l[j]
        if (a>_a) == (b>_b):
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            pass
print(N-max(dp))