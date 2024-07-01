#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1351                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1351                          #+#        #+#      #+#     #
#     Solved: 2024-05-29 15:29:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,P,Q = map(int, input().split())
dp = dict()
X = min(P,Q)
 
def recur(n):
    if not n:
        return 1
    if n < X:
        return 2
    if n in dp:
        return dp[n]
 
    np, nq = n//P, n//Q
    dp[np] = recur(np)
    dp[nq] = recur(nq)
    return dp[np] + dp[nq]
print(recur(N))