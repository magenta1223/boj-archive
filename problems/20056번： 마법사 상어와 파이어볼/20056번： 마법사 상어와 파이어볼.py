#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 20056                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/20056                         #+#        #+#      #+#     #
#     Solved: 2024-02-21 17:04:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
N, M, K = map(int, input().split())
fire = []
for _ in range(M):
    r, c, *_ = map(int, input().split())
    fire.append((r-1, c-1, *_))
 
 
for _ in range(K):
    # move fire
    newFire = {} # {(row, col): [mass, speed, direction, cnt]} 
    for r, c, m, s, d in fire:
        dr, dc = delta[d]
        r, c = (r + (dr+N)*s) % N, (c + (dc+N)*s) % N
        if (r, c) in newFire:
            nm, ns, nd, cnt = newFire[(r, c)]
            if nd != 9 and nd % 2 == d % 2: # compare direction
                newFire[(r, c)] = [nm + m, ns + s, nd % 2, cnt + 1] # to 0, 2, 4, 6
            else:
                newFire[(r, c)] = [nm + m, ns + s, 9, cnt + 1] # to 1, 3, 5, 7
        else:
            newFire[(r, c)] = [m, s, d, 1] # to d
 
    # next fire
    fire.clear()
    for r, c in newFire:
        m, s, d, cnt = newFire[(r, c)]
        if cnt > 1:
            if m < 5: continue # fire disappear
            m, s =  m // 5, s // cnt
            if d == 9:
                for nd in (1, 3, 5, 7):
                    fire.append((r, c, m, s, nd))
            else:
                for nd in (0, 2, 4, 6):
                    fire.append((r, c, m, s, nd))
        else:
            fire.append((r, c, m, s, d))
 
 
ans = 0
for ball in fire:
    ans += ball[2]
print(ans)