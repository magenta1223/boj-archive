#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4949                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4949                          #+#        #+#      #+#     #
#     Solved: 2023-11-22 13:41:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input=sys.stdin.readline
pair={')':'(',']':'['}
while True:
    strs=input().rstrip()
    if strs==".":
        break
    hist=''
    invalid=False
    for s in strs:
        if s in '([':
            hist+=s
        elif s in ')]':
            if hist and hist[-1] == pair[s]:
                hist=hist[:-1]
            else:
                invalid=True
                break
    if hist or invalid:
        print("no")
    else:
        print("yes")
            