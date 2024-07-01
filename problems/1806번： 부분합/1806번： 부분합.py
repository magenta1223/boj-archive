#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1806                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1806                          #+#        #+#      #+#     #
#     Solved: 2024-01-31 21:19:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,S=map(int, input().split())
l=list(map(int, input().split()))
 
a,b=0,0
s = 0
min_length = float("inf")
while a<N:
    if s < S:
        if b <= N-1:
            # print("lower", a,b,s)
            s += l[b]
            b += 1
        else:
            break 
    else:
        # S 이상인가 -> 제거 
        # print("upper", a,b,s)
        min_length=min(b-a, min_length)
        s -= l[a]
        a += 1
        
print(min_length if min_length != float("inf") else 0)