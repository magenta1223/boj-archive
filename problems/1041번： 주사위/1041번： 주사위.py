#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1041                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1041                          #+#        #+#      #+#     #
#     Solved: 2024-05-24 11:11:32 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
a,b,c,d,e,f=map(int,input().split())
 
if N==1:
    print(sum([a,b,c,d,e,f]) - max([a,b,c,d,e,f]))
    exit(0)
 
adj2= [(a,b), (a,c), (a,d), (a,e), (f,b), (f,c), (f,d), (f,e), (b,c), (b,d), (c,e), (d,e)]
adj3 = [(a,b,c), (a,b,d), (a,d,e), (a,c,e), (f,b,c), (f,b,d), (f,d,e), (f,c,e)]
s1 = min([a,b,c,d,e,f])
s2 = min([sum(s) for s in adj2])
s3 = min([sum(s) for s in adj3]) 
ans = s1*(5*(N**2)-16*N+12) + s2*(8*N-12) + s3*4
print(ans)