#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1099                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1099                          #+#        #+#      #+#     #
#     Solved: 2024-05-27 09:33:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S=input().strip()
M = len(S)
N=int(input())
W = [input().strip() for _ in range(N)]
 
INF = float("inf")
dp = [INF] * (M+1)
 
# top-down 
s,e = 0,1 
 
def calc_cost(w1, w2):
    # w1을 기준, w2를 만드는 비용 
    return sum([1 for i in range(len(w1)) if w1[i] != w2[i]])
 
dp[0] = 0
for s in range(M):
    for e in range(s+1, M+1):
        # print("CHECK", S[s:e])
        w_candidate = sorted(S[s:e])
        for w in W:
            # print('--MATCH', w)
            if sorted(w) == w_candidate:
                # print("----CORRECT")
                # 비용 계산. 
                # dp[e]에 저장 
                dp[e] = min(dp[e], dp[s] + calc_cost(w, S[s:e])) 
 
print(dp[M] if dp[M] != INF else -1)