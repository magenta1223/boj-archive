#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15651                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15651                         #+#        #+#      #+#     #
#     Solved: 2023-11-28 11:55:23 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M=map(int, input().split())
# bfs
def bfs(ls, depth):
    newls=[]
    for l in ls:
        for i in range(1,N+1):
            newl=l+[i]
            newls.append(newl)
    if depth+1==M:
        return newls
    else:
        return bfs(newls, depth+1)
 
for l in bfs([[]], 0):
    l = [str(e) for e in l]
    if len(l) == 1:
        print(l[0])
    else:
        print(" ".join(l))