#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1316                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1316                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 15:28:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
 
count = N
for _ in range(N):
    word = input()
    s_set= set()
    prev_s = ""
    for s in word:
        if s in s_set:
            count -= 1
            break 
        elif s == prev_s:
            continue
        else:
            s_set.add(prev_s)
            prev_s = s
    
print(count)