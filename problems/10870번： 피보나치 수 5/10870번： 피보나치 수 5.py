#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10870                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10870                         #+#        #+#      #+#     #
#     Solved: 2023-11-24 15:15:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def fibonacci(hist, n):
    if len(hist) == n:
        if n==0:
            return 0
        else:
            return hist[-1]
    else:
        if not hist:
            hist.append(1)
        elif len(hist) == 1:
            hist.append(1)
        else:
            hist.append(hist[-2]+hist[-1])
        return fibonacci(hist, n)
print(fibonacci([],int(input())))