#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7579                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7579                          #+#        #+#      #+#     #
#     Solved: 2023-12-28 16:25:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
mem=list(map(int, input().split()))
cost=list(map(int, input().split()))
 
maxC = sum(cost)
dp = [0] * (maxC+1)
 
for i in range(len(mem)):
    m = mem[i]
    c = cost[i]
    for j in range(maxC, c-1, -1):
        # j원으로 확보 가능한 최대 메모리를 저장. 
        # j-c원 최대 메모리 + 추가메모리 vs j원 메모리 
        dp[j] = max(dp[j-c] + m, dp[j])
 
for i, d in enumerate(dp):
    if d >= M:
        print(i)
        break