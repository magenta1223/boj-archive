#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 6064                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/6064                          #+#        #+#      #+#     #
#     Solved: 2024-03-07 22:56:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solve(m,n,x,y):
    # x를 맞춰놓고 y를 따라가기
    ans = x 
    while ans <= m*n:
        if (ans - x) % m == 0 and (ans - y) % n == 0: # 왜 다르지/
            return ans 
        ans += m 
    return -1 
    
    
for _ in range(int(input())):
    print(solve(*map(int,input().split())))