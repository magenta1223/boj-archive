#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3273                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3273                          #+#        #+#      #+#     #
#     Solved: 2024-01-31 11:32:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n = int(input().strip())
l = list(map(int, input().split()))
x = int(input().strip())
def count_pairs(arr, x):
    count = 0
    elements = set()
    for a in arr:
        if x - a in elements:
            count += 1
        elements.add(a)
    return count
 
 
print(count_pairs(l, x))