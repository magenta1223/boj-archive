#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2493                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2493                          #+#        #+#      #+#     #
#     Solved: 2024-07-01 11:56:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N = int(input())
TOWER = list(map(int,input().split()))
 
ans, stack = [], []
for i in range(N):
    t = TOWER[i]
    while stack and TOWER[stack[-1]] < t:
        stack.pop()
 
    if stack and TOWER[stack[-1]] > t:
        ans.append(stack[-1]+1)
    else:
        ans.append(0)
    stack.append(i)
print(*ans)