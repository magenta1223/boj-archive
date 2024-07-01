#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9251                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9251                          #+#        #+#      #+#     #
#     Solved: 2023-12-20 13:40:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

seqA = input().strip()
seqB = input().strip()
# dp[i][j] : seqA[:i]와 seqB[:j]를 가지고 만든 LCS의 길이 
dp = [[0] * (len(seqB) + 1) for _ in range(len(seqA) + 1)]
 
for i in range(1, len(seqA) + 1):
    for j in range(1, len(seqB) + 1):
        if seqA[i - 1] == seqB[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else: # 불일치 시 이전 값을 그냥 더함. 
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
 
print(dp[-1][-1])