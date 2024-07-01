#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11812                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11812                         #+#        #+#      #+#     #
#     Solved: 2024-03-12 16:47:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
def solve():
    x,y = map(int,input().split())    
    if K==1:
        return abs(x-y)
 
    ans = 0
    while x != y: 
        # 다르면 -> 큰쪽을 줄이면 됨 
        if y<x:
            x,y = y,x 
        y = (y-2) // K + 1
        ans += 1
    return ans 
    
N,K,Q = map(int,input().split())
for _ in range(Q):
    print(solve())