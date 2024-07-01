#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2166                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2166                          #+#        #+#      #+#     #
#     Solved: 2024-04-05 13:48:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
def tri(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2) * 0.5
N = int(input())
COORDS = [list(map(int, input().split())) for _ in range(N)]
a = COORDS[0]
ans = 0 
for i in range(1, N-1):
    b,c = COORDS[i], COORDS[i+1]
    ans += tri(*a,*b,*c)
print(round(abs(ans), 2))