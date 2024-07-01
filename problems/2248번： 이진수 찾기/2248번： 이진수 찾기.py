#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2248                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2248                          #+#        #+#      #+#     #
#     Solved: 2024-03-28 15:08:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,L,I = map(int,input().split())
dp = [[0] * (L+1) for _ in range(N+1)]
# X 자리에서 0개 사용하는 방법 = 1
for i in range(N+1):
    dp[i][0] = 1 
 
for i in range(1,N+1):
    for j in range(1,min(i+1,L+1)):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
 
ans = ""
while N:
    leading_zero = sum(dp[N-1][:L+1])
    if I > leading_zero:
        ans += "1"
        L-=1 
        I-=leading_zero
    else:
        ans+="0"
    N-=1 
print(ans)