#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4153                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4153                          #+#        #+#      #+#     #
#     Solved: 2024-04-04 14:28:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def calc(a,b,c):
    a,b,c = sorted([a,b,c])
    print("right" if a**2 + b**2 == c**2 else "wrong")
 
while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break 
    calc(a,b,c)