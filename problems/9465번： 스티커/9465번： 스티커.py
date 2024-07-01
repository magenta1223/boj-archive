#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9465                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9465                          #+#        #+#      #+#     #
#     Solved: 2024-03-13 17:44:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(arr, n):
    dp = [[0] * n for _ in range(2)] 
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    for i in range(1,n):
        for j in range(2):
            # 대각선 방향 스티커+현재값, 좌측값 비교 
            dp[j][i] = max([dp[1-j][i-1]+arr[j][i], dp[j][i-1]])
    return max(dp[-1][-1], dp[0][-1])
 
for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]
    print(solve(arr,n))