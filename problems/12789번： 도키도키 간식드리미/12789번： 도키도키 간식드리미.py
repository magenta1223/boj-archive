#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12789                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12789                         #+#        #+#      #+#     #
#     Solved: 2023-11-22 14:02:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
now=list(map(int, input().split()))
new=[]
f= 1
for x in now:
    if x == f:
        f+=1
    else:
        new.append(x)
    while new and new[-1] == f:
        f+=1
        new.pop()
if new:
    print("Sad")
else:
    print("Nice")