#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10844                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10844                         #+#        #+#      #+#     #
#     Solved: 2023-12-19 14:44:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
array=[1 for i in range(10)]
 
for i in range(1, N):
    new_array = [a for a in array]
    for j, a in enumerate(array):
        if j == 0:
            new_array[j] = array[1]
        elif j == 9:
            new_array[9] = array[8]
        else:
            new_array[j] = array[j-1] + array[j+1]        
    array = new_array
    
print(sum(array[1:]) % 1_000_000_000)