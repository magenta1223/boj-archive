#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13305                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13305                         #+#        #+#      #+#     #
#     Solved: 2023-12-21 16:53:53 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
dists=list(map(int, input().split()))
costs=list(map(int, input().split()))
costs = [ (i,c) for i, c in enumerate(costs)]
costs.sort(key= lambda x: x[1])
prev_i = N
ans = 0
for i, c in costs:
    if prev_i > i:
        ans += sum(dists[i:prev_i]) * c 
        prev_i = i
print(ans)