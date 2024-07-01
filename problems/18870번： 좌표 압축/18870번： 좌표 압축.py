#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 18870                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/18870                         #+#        #+#      #+#     #
#     Solved: 2023-10-26 17:49:24 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# xs = map(int, [*open(0)][1:].split())
 
import sys
input = sys.stdin.readline
n = int(input())
xs = list(map(int, input().rstrip().split()))
xlst = sorted(list(set(xs)))
dictList = dict(zip(xlst,list(range(len(xlst)))))
print(*[dictList[x] for x in xs])