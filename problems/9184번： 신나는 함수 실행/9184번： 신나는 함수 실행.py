#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9184                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9184                          #+#        #+#      #+#     #
#     Solved: 2023-12-18 20:47:51 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]    
for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]           
while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break 
    
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = {w[0][0][0]}")
    elif a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = {w[20][20][20]}")
    else:
        print(f"w({a}, {b}, {c}) = {w[a][b][c]}")