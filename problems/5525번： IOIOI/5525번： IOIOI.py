#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5525                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5525                          #+#        #+#      #+#     #
#     Solved: 2024-03-07 22:22:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
M = int(input())
S = input().strip()
 
Pn = "IO" * N + "I"
ans = 0
streak = 0
i = 0
while i < M:
    # io가 나오는지? 
    if S[i:i+2] == "IO":
        # streak 
        streak += 1
        i += 2
    else:
        i += 1
        streak = 0 
    if i >= M:
        break
    if streak >= N and S[i] == "I":
        ans += 1 
 
print(ans)