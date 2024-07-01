#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2568                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2568                          #+#        #+#      #+#     #
#     Solved: 2024-04-11 16:12:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from bisect import bisect_left 
input = open(0).readline 
N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
L.sort(key = lambda x: x[0])
 
stack = []
indices = []
prev = [-1] * N
As = []
 
for i in range(N):
    a,b = L[i]
    As.append(a)
    idx = bisect_left(stack, b)
    if idx == len(stack):
        stack.append(b)
        indices.append(i)
    else:
        stack[idx] = b
        indices[idx] = i
    if idx > 0:
        prev[i] = indices[idx-1]
 
 
valid = set()
idx = indices[-1] # 가장 마지막 원소의 index
 
 
while idx != -1:
    valid.add(As[idx]) # 역으로 거슬러 올라가며 더함 
    idx = prev[idx] # 
                
print(N - len(stack))
print(*set(As) - valid, sep = '\n')