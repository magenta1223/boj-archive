#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11256                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11256                         #+#        #+#      #+#     #
#     Solved: 2024-06-13 19:56:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

for _ in range(int(input())):
    J,N = map(int,input().split())
    
    capacities = []
    for _ in range(N):
        R,C = map(int,input().split())
        capacities.append(R*C)
 
    capacities.sort(reverse=True)
 
    ans, candy = 0, 0
    for i in range(N):
        candy += capacities[i]
        ans += 1
        if candy >= J:
            break 
 
    print(ans) 