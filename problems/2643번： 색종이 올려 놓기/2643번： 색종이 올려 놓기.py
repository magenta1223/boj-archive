#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2643                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2643                          #+#        #+#      #+#     #
#     Solved: 2024-07-23 02:41:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# P안의 색종이들을
# 1. 변이 평행 or 수직이도록 위에 쌓아 올린다
# 2. 아래 색종이가 위 색종이보다 커야한다. 

# 색종이는 최대 100장, 변의 길이는 최대 1000 
# 그냥하면 100! -> dp or greedy 




N = int(input())
P = [sorted(list(map(int,input().split()))) for _ in range(N)] 
P.sort(key = lambda x: (x[1], x[0]))

def check(i,j):
    a,b = P[i]
    c,d = P[j]
    if (a>=c and b>=d) or (a>=d and b>=c):
        return True 
    else:
        return False 
    

dp = [-1] * N 
def dfs(idx):
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = 1
    res = 0  
    for i in range(idx+1, N):
        if check(i, idx):
            res = max(res, dfs(i))
    dp[idx] += res 
    return dp[idx]

for i in range(N):
    dfs(i)

print(max(dp))

