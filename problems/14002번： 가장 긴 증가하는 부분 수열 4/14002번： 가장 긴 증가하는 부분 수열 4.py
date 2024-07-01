#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14002                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14002                         #+#        #+#      #+#     #
#     Solved: 2024-02-05 18:34:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
L=list(map(int, input().split()))
 
 
dp = [1] * N
H = [[L[i]] for i in range(N)] 
 
for j in range(N): # j번째에서 종료
    for i in range(j): # i번째에서 시작 
        if L[j] > L[i]: # 더할 수 있음. 
            if dp[j] < dp[i] + 1:
                dp[j] = dp[i] + 1
                H[j] = H[i] + [L[j]]
                
                
x = dp.index(max(dp))        
print(dp[x])
print(*H[x])