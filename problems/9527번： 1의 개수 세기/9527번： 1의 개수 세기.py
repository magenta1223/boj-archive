#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9527                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9527                          #+#        #+#      #+#     #
#     Solved: 2024-04-08 19:55:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def calc(x):
    count, w = 0, 1 
    while x:
        if x == 1:
            count += w
            break 
        if not x % 2:
            count += bin(x).count('1') * w
            x -= 1 
            continue
    
        x = (x-1) // 2 
        count += (x+1)*w
        w *= 2 
    return count 
 
A, B = map(int, input().split())
print(calc(B) - calc(A-1))