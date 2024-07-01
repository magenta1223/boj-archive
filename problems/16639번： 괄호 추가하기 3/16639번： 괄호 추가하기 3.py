#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16639                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16639                         #+#        #+#      #+#     #
#     Solved: 2024-05-07 15:40:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
EQ = input().strip()
 
INF = float("inf")
dp = [[[INF, -INF] for _ in range(N+1)] for _ in range(N+1)]
 
for k in range(0,(N+1),2):
    v = int(EQ[k])
    dp[k][k] = [v, v] 
 
 
def dfs(s,e,d):
    if s == e:
        return dp[s][e][0]
 
    if dp[s][e][0] != INF:
        return dp[s][e][0]
 
    res = eval(f"{EQ[s:e+1]}") 
    _min, _max = res, res 
 
    for i in range(s,e,2):
        for j in range(i+2,e+1,2):
            if (i,j) == (s,e):
                continue
 
 
            dfs(i,j,d+1)
            if s != i:
                dfs(s,i-2,d+1)
            if e != j:
                dfs(j+2,e,d+1)
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        new_eq = ""
                        if s != i:
                            new_eq += f"{dp[s][i-2][a]}{EQ[i-1]}"
                        new_eq += str(dp[i][j][b])
                        if e != j:
                            new_eq += f"{EQ[j+1]}{dp[j+2][e][c]}"
 
                        res = eval(new_eq)
                        _min = min(_min, res)
                        _max = max(_max, res)
 
    dp[s][e] = _min, _max 
 
dfs(0,N-1,1)
print(dp[0][N-1][1])