#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2447                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2447                          #+#        #+#      #+#     #
#     Solved: 2023-11-24 17:12:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def func(n):
    if n==1:
        return ["*"]
    else:
        block=func(n//3)
        big_block=[]
        for b in block:
            big_block.append(b*3)
        for b in block:
            big_block.append(b+" "*(n//3)+b)
        for b in block:
            big_block.append(b*3)
        return big_block
    
print(*func(int(input())), sep="\n")