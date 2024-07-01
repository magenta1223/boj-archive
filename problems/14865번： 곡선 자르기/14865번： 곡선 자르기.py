#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14865                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14865                         #+#        #+#      #+#     #
#     Solved: 2024-05-31 14:06:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
N=int(input())
COORDS = [tuple(map(int,input().split())) for _ in range(N)]
 
x = sorted(COORDS, key = lambda x:(x[1]))[0]
idx = COORDS.index(x)
COORDS = COORDS[idx:] + COORDS[:idx] + [COORDS[idx]]
 
start,px,py = None,0,0
mountains = []
for i in range(len(COORDS)):
    x,y = COORDS[i]
    if y*py < 0:
        # 
        if start is None:
            start = x 
        else:
            mountains.append(tuple(sorted([start,x])))
            start = None 
    px,py = x,y 
mountains.sort()
 
# 이제 푼다
# 포함관계인지? 
def isIncluded(m1, m2):
    s1, e1 = m1 
    s2, e2 = m2 
    return e1 > s2 
 
_mountains = sorted(mountains, key = lambda x:x[1])
s,e = _mountains[-1]
mountains.append((e+1, e+2))
 
ans1, ans2 = 0,0 
stack = []
for i in range(len(mountains)):
    # 마지막 산에 포함..? 을 확인
    if stack and not isIncluded(mountains[stack[-1]], mountains[i]):
        ans2 += 1 
    while stack and not isIncluded(mountains[stack[-1]], mountains[i]):
        stack.pop()
    # stack이 비어있다 -> 최상위 산임. 
    if not stack:
        ans1 += 1 
    stack.append(i)
print(ans1-1, ans2)