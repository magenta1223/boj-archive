#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1629                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1629                          #+#        #+#      #+#     #
#     Solved: 2023-12-21 18:23:01 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

A,B,C=map(int, input().split())
 
def func(a,b):
    if b == 1:
        return a%C
    else:
        tmp = func(a, b//2)
        if not b%2:
            return (tmp*tmp)%C
        else:
            return (tmp*tmp*A)%C
print(func(A,B))