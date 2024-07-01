#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14425                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14425                         #+#        #+#      #+#     #
#     Solved: 2023-11-02 13:35:46 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
N, M = map(int, input().split())
sA = { input() for _ in range(N)}
print( sum( [ 1 if input() in sA else 0 for _ in range(M)]  ) )