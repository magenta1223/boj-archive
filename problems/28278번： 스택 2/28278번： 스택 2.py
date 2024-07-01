#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 28278                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/28278                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 13:17:05 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
N=int(input())
stack=[]
for _ in range(N):
    c=input()
    
    if len(c.split()) > 1:
        c, n = map(int, c.split())
    else:
        c = int(c)
    if c == 1:
        stack.append(n)
    elif c==2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c==3:
        print(len(stack))
    elif c==4:
        print(int(len(stack) == 0)) 
    else:
        if stack:
            print(stack[-1]) 
        else:
            print(-1)
 