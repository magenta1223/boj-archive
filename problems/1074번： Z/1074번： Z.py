#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1074                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1074                          #+#        #+#      #+#     #
#     Solved: 2024-03-04 20:50:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def recur(N, r, c, ans):
    if N == 2:
        return ans + r*2 + c
    next_N = (N//2)
    a = 1 if r >= next_N else 0 
    b = 1 if c >= next_N else 0
    ans += (2*a + b) * (next_N ** 2)
    r, c = r - a*next_N, c - b*next_N  
    if not r and not c :
        return ans 
    else:
        return recur(next_N, r,c, ans)
 
N,r,c = map(int,input().split())
N = 2**N
print(recur(N, r,c, 0))