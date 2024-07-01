#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17420                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17420                         #+#        #+#      #+#     #
#     Solved: 2024-06-18 10:38:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil 
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
 
C = [(A[i], B[i], i) for i in range(N)] 
C.sort(key= lambda x:(x[1], x[0]))
    
ans =0 
prev_plan = -1
th1, th2 = -1, -1 
 
for i in range(N):
    exp,plan,idx = C[i]
 
    # 가장 최근에 기프티콘 사용한 날짜 보다만 크면 됨. 
    if prev_plan != plan:
        th1 = max(th1, th2, plan) 
        th2 = 0
    
    if th1 > exp:
        cnt = ceil((th1-exp) / 30)
    else:
        cnt = 0
 
    A[idx] = exp+30*cnt  
    ans += cnt 
    prev_plan = plan
    th2 = max(th2, A[idx])
 
print(ans)