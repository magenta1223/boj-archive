#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9252                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9252                          #+#        #+#      #+#     #
#     Solved: 2024-02-06 13:15:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

seqA = input().strip()
seqB = input().strip()
 
# seqA[:i]와 seqB[:j]로 만들 수 있는 LCS의 길이를 저장 
dp = [ [0] * (len(seqB)+1) for _ in range(len(seqA)+1)]
H = [ [""] * (len(seqB)+1) for _ in range(len(seqA)+1)]
 
for i in range(1,len(seqA)+1):
    for j in range(1,len(seqB)+1):
        # LCS로 만들 수 있는지? = 글자가 같은지
        if seqA[i-1] == seqB[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 
            H[i][j] = H[i-1][j-1] + seqA[i-1] 
        elif dp[i-1][j] > dp[i][j-1]:
            dp[i][j] = dp[i-1][j]
            H[i][j] =  H[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]
            H[i][j] =  H[i][j-1]
 
if dp[-1][-1]:
    print(dp[-1][-1])
    print(H[-1][-1])
else:
    print(dp[-1][-1])