#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2738                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2738                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 15:40:30 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
 
A = []
for _ in range(N):
    line = list(map(int, input().split()))
    A.append(line)
    
AB = []
for i in range(N):
    line = list(map(int, input().split()))
    A_line = A[i]
    new_line = [ str(a+b) for a, b in zip(A_line, line)]
    AB.append(new_line)
 
for l in AB:
    print(" ".join(l))