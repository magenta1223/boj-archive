#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7869                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7869                          #+#        #+#      #+#     #
#     Solved: 2024-06-13 11:56:55 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt, acos, sin, pi 
 
x1, y1, r1, x2, y2, r2 = map(float, input().split())
 
# 두 점에서 만나는지? 
d2 = (x2-x1)**2 + (y2-y1)**2 
d = sqrt((x2-x1)**2 + (y2-y1)**2 )
if r1+r2 <= d :
    ans = 0
elif d+min(r1,r2) <= max(r1,r2):
    ans =pi * (min(r1,r2)**2) 
else:
    theta1 = acos((r1**2 + d2 - r2**2) / (2*r1*d))*2
    theta2 = acos((r2**2 + d2 - r1**2) / (2*r2*d))*2
 
    def calc(r, theta):
        return 0.5*(r**2)*(theta - sin(theta))
    ans = calc(r1, theta1) + calc(r2, theta2)
 
print(f"{ans:.3f}")