#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2632                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2632                          #+#        #+#      #+#     #
#     Solved: 2024-05-21 09:32:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
S=int(input())
M,N=map(int,input().split())
PIZZA_A = [int(input()) for _ in range(M)]
PIZZA_B = [int(input()) for _ in range(N)]
 
def solve(pizza):
    dp = [0] * (S+1)
    n_piece = len(pizza)
    for i in range(n_piece):
        _pizza = pizza[i:] + pizza[:i]
        s = 0
        for j in range(n_piece):
            assert pizza[(i+j)%n_piece] == _pizza[j], "ssibal"
            s += _pizza[j]
            if s <= S:
                dp[s] += 1
 
    if sum(pizza) <= S:
        dp[sum(pizza)] = 1
    return dp 
 
dp_a = solve(PIZZA_A)
dp_b = solve(PIZZA_B)
dp_a[0], dp_b[0] = 1,1
 
 
ans = 0
for i in range(S+1):
    ans += dp_a[i]*dp_b[S-i]
print(ans)