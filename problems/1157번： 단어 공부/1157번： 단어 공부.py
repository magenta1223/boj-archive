#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1157                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1157                          #+#        #+#      #+#     #
#     Solved: 2023-10-17 15:05:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

x = input().lower()
m = 0
most_used = ""
for l in set(x):
    if x.count(l) > m:
        most_used = l.upper()
        m = x.count(l)
    elif x.count(l) == m:
        most_used = "?"
    
print(most_used)