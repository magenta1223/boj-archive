#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1463                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1463                          #+#        #+#      #+#     #
#     Solved: 2023-12-19 11:56:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
default_value = 0
array = [default_value for _ in range(N+1)]
for i in range(1,N):
    num_oper = array[i]
    if 3*i < N+1:
        if array[3*i] == default_value or array[3*i] > num_oper+1:
            array[3*i] = num_oper+1 
    if 2*i < N+1:
        if array[2*i] == default_value or array[2*i] > num_oper+1:
            array[2*i] = num_oper+1 
    if array[i+1] == default_value or array[i+1] > num_oper+1:
        array[i+1] = num_oper+1
print(array[-1])