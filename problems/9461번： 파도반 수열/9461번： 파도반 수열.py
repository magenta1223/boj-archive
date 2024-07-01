#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9461                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9461                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 22:10:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T = int(input())
def func(n):
    if n <= 3:
        return 1
    arr = [1 for _ in range(n)]
    for i in range(3, n):
        arr[i] = arr[i-2] + arr[i-3]
    return arr[n-1]
 
for _ in range(T):
    print(func(int(input())))