#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2216                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2216                          #+#        #+#      #+#     #
#     Solved: 2024-03-27 16:55:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def score(a,b):
    if a == " " or b == " ":
        return B 
    return A if a==b else C
A,B,C = map(int, input().split())
X,Y = " " +  input().strip(), " " + input().strip()
N, M = len(X), len(Y)
dp = [[0] * (M) for _ in range(N)]
for i in range(N):
    dp[i][0] = B*i
for j in range(M):
    dp[0][j] = B*j
 
for i in range(1,N):
    for j in range(1,M):
        dp[i][j] = max([
            dp[i-1][j] + score(X[i], " "),
            dp[i][j-1] + score(" ", Y[j]),
            dp[i-1][j-1] + score(X[i], Y[j]),
        ])
print(dp[-1][-1])