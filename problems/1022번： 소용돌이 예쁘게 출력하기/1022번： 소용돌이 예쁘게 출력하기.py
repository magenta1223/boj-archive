#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1022                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1022                          #+#        #+#      #+#     #
#     Solved: 2024-06-14 10:47:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

r1,c1,r2,c2 = map(int,input().split())
 
def findX(x,y):
    k = max(abs(x), abs(y))
    if x<y:
        if y==k: 
            sx,sy = k-1, k
            dx, dy = -1, 0 
            idx = (x-sx)*dx             
        else:
            sx,sy = -k, k-1
            dx, dy = 0, -1
            idx = (y-sy)*dy + 2*k
    elif x==y:
        if x < 0:
            sx,sy = -k, k-1
            dx, dy = 0, -1
            idx = (y-sy)*dy +2*k
        else:
            sx,sy = k, -k+1 
            dx, dy = 0, 1
            idx = (y-sy)*dy + 6*k
    else:
        if y==-k:
            sx,sy = -k+1, -k 
            dx, dy = 1,0 
            idx = (x-sx)*dx + 4*k
        else:
            sx,sy = k, -k+1 
            dx, dy = 0, 1
            idx = (y-sy)*dy +6*k
    return (2*k-1) ** 2 + idx+1
 
arr = []
for r in range(r1,r2+1):
    arr.append([findX(r,c)  for c in range(c1,c2+1)])
        
maxlen = 1 
for row in arr:
    maxlen = max(maxlen, max([len(str(num)) for num in row]))
 
def blankfill(num):
    num = str(num)
    return " "*(maxlen-len(num))+num 
 
for row in arr:
    print(*[ blankfill(num) for num in row])