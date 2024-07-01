#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1637                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1637                          #+#        #+#      #+#     #
#     Solved: 2024-03-12 17:37:49 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil 
input = open(0).readline
N = int(input())
integers = [list(map(int,input().split())) for _ in range(N)]
 
def get_num(a,c,b,th):
    th = min(c,th)
    if th < a:
        return 0
    else:
        return ceil((th-a) // b) + 1
    
        
def solve(integers):
    s,e = 0, 2_147_483_647
    while s <= e:
        mid = (s+e)//2 
        total = sum([get_num(a,c,b,mid) for a,c,b in integers])
        if total % 2:
            e = mid-1
        else:
            s = mid+1
            
 
    cnt = sum([get_num(a,c,b,s) for a,c,b in integers]) - sum([get_num(a,c,b,s-1) for a,c,b in integers])
    if cnt % 2:
        print(s, cnt)
    else:
        print("NOTHING")
 
 
solve(integers)
 