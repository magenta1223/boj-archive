#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1181                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1181                          #+#        #+#      #+#     #
#     Solved: 2023-10-26 17:26:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n = int(input())
lst = []
for i in range(n):
    lst.append(input())
lst= list(set(lst))
strs = sorted(lst, key = lambda x : (len(x), x))
for s in strs:
    print(s)