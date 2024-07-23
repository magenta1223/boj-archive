#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2718                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2718                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 04:37:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def calc(i):
    if i == 1:
        return 1 
    elif i == 2:
        return 4
    elif i%2:
        return 2 
    else:
        return 3 


for _ in range(int(input())):
    N = int(input())
    dp = [0] * 23 # 22에서 4_977_472_781 가지 
    dp[1] = 1 
    dp[2] = 5 
    for i in range(3,N+1):
        for j in range(1,i):
            dp[i] += dp[j] * calc(i-j)
        if i%2:
            dp[i] += 2  
        else:
            dp[i] += 3 
    print(dp[N]) 