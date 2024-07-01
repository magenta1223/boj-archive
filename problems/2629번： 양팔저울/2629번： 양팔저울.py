#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2629                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2629                          #+#        #+#      #+#     #
#     Solved: 2023-12-28 12:54:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0, "rb").readline
 
N=int(input())
W=list(map(int, input().split())) # 추
M=int(input())
B=list(map(int, input().split())) # 구슬
 
maxW = sum(W)
dp = [[False] * (3*N) for _ in range(maxW*2+1)] 
dp[maxW][-1] = True 
 
def dfs(i, weight):
    if i == N: # 여기도 아님. w
        return     
    
    for j, w in enumerate([-1, 0, 1]):
        newW = weight + W[i]*w
        if not dp[newW][3*i+j]:
            dfs(i+1, newW)
            dp[newW][3*i+j] = True 
 
def check(dp, b, maxW):
    if b > maxW:
        return "N"
    elif sum(dp[b]):
        return "Y" 
    else:
        return "N" 
dfs(0, 0)
print(*[ check(dp, b, maxW) for b in B])