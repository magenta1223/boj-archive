#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1744                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1744                          #+#        #+#      #+#     #
#     Solved: 2024-05-23 16:19:42 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
p, n,z = [], [], False 
for _ in range(N):
    a  = int(input())
    if a < 0:
        n.append(a)
    elif a > 0:
        p.append(a)
    else:
        z = True  
 
p.sort(reverse= True)
n.sort()
 
ans = 0
for i in range(0,len(p)-1, 2):
    if p[i]*p[i+1] > p[i]+p[i+1]:
        ans += p[i]*p[i+1]
    else:
        ans += sum(p[i:])
        break
else:
    if len(p) % 2:
        ans += p[-1]
 
 
for i in range(0,len(n)-1,2):
    ans += n[i]*n[i+1]
if len(n) % 2:
    if not z:
        ans += n[-1]
 
print(ans)