#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1701                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1701                          #+#        #+#      #+#     #
#     Solved: 2024-04-13 12:00:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S = input().strip()
N = len(S)
ans = 1
idx = 0
while idx + ans <= N:
    substr = S[idx:idx+ans]
    another = False   
    for i in range(idx+1, N+1-ans):
        if substr == S[i:i+ans]:
            another = True 
            break 
    if another:
        ans += 1 
    else:
        idx += 1 
print(ans-1)