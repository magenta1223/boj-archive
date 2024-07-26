#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11402                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11402                         #+#        #+#      #+#     #
#     Solved: 2024-07-25 00:19:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# (N K)를 M으로 나눈 나머지 
# 대충봐도 M by M으로 하는건데 


# https://ko.wikipedia.org/wiki/%EB%A4%BC%EC%B9%B4%EC%9D%98_%EC%A0%95%EB%A6%AC
# 1. N과 K를 M에 대해 표현 -> N = N_k*M^K + ... + N_1*M + N_0 
# 2. 계수 N_k, K_k 는 전부 m이하
# 3. 최대 M까지 모든 이항계수를 구하고 인덱싱하면됨 


def serialize(x:int, p:int):
    xs = []
    while x:
        x, xi = divmod(x,p)
        xs.append(xi)
    return xs 
N,K,M = map(int, input().split())
Ns = serialize(N,M)
Ks = serialize(K,M)
maxlen = max(len(Ns), len(Ks))
Ns = Ns + [0] * (maxlen - len(Ns))
Ks = Ks + [0] * (maxlen - len(Ks))

dp = [[0] * (M+1) for _ in range(M+1)]
dp[1][1] = 1 
for i in range(M+1):
    dp[i][0] = 1

for i in range(1,M+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

ans = 1 
for n,k in zip(Ns, Ks):
    ans *= dp[n][k]
    ans %= M 
print(ans)

