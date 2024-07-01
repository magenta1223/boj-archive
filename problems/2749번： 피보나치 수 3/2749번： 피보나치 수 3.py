#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2749                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2749                          #+#        #+#      #+#     #
#     Solved: 2024-02-27 18:47:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
l = [0,1]
 
if N <= 1:
    print(l[N])
else:
    i = 2
    ans = 0
    period = 0
    vs = [0,1]
    # 반복되는 주기가 있음. 주기를 찾기     
    while i <= N:
        ans = sum(l) % 1_000_000
        l = [l[1], ans]
        vs.append(ans)
        if l == [0,1]:
            period = i - 1
            break 
        i += 1
 
    print(vs[N % (i-1)] if period else ans)