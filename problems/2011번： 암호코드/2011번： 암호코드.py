#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2011                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2011                          #+#        #+#      #+#     #
#     Solved: 2024-03-15 15:33:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 불가능한 입력
# case 1. 0으로 시작
# case 2. 0앞의 수가 3 이상 
# case 3. 100000 같이 연속한 0이 2개 이상 나옴 
 
encoded=list(map(int, input().strip()))
# case 1
if encoded[0] == 0:
    print(0)
    exit(0)
 
for i in range(len(encoded)-1, -1, -1):
    if not encoded[i]:
        # case 2, 3 
        if encoded[i-1] > 2 or not encoded[i-1]:
            print(0)
            exit(0)
        encoded[i-1] = int(str(encoded[i-1]) + "0")
        del encoded[i]
 
N = len(encoded)
dp = [0] * (N+1) 
dp[0] = 1
dp[1] = 1
for i in range(2,N+1):
    if encoded[i-2] < 10:
        dp[i] = dp[i-1]
        if int(str(encoded[i-2]) + str(encoded[i-1])) < 27:
            dp[i] += dp[i-2]
        dp[i] %= 1000000
    else:
        dp[i] = dp[i-1]
print(dp[-1])