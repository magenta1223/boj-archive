#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9177                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9177                          #+#        #+#      #+#     #
#     Solved: 2024-03-12 10:39:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(w1, w2, w3):
    w1 = " " + w1 
    w2 = " " + w2 
    w3 = " " + w3 
    
    N,M=len(w1), len(w2)
    dp = [[False] * M for _ in range(N)]
    dp[0][0] = True 
    # dp[i][j] = w1[:i+1] and w2[:j+1]을 이용해 w3를 만들 수 있는지? 
    # w1[:i], w2[:j+1] 까지 했는데 -> 됐다! -> 여기에 w[i] == w3[i+j+1]이라면 삽가능     
    for i in range(N):
        for j in range(M):
            if not i and not j:
                continue                
            dp[i][j] = (w1[i] == w3[i+j] and dp[i-1][j]) or (w2[j] == w3[i+j] and dp[i][j-1])
            
    return "yes" if dp[-1][-1] else "no" 
 
 
 
for i in range(1, int(input())+1):
    w1, w2, w3 = input().split()
    print(f"Data set {i}: {solve(w1,w2,w3)}")
 