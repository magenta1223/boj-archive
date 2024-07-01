#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16287                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16287                         #+#        #+#      #+#     #
#     Solved: 2024-06-03 16:52:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

W,N= map(int,input().split())
A = list(map(int,input().split()))
 
dp = [False] * (W+1)
for i in range(N):
    for j in range(i+1, N):
        if A[i]+A[j] < W+1:
            dp[A[i]+A[j]] = (i,j) 
 
for i in range(N):
    for j in range(i+1, N):
        w =A[i]+A[j]  
        if w > W or not dp[W-w]:
            continue 
        if i not in dp[W-w] and j not in dp[W-w]:
            print("YES")
            exit(0)
print("NO")