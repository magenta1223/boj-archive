#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1493                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1493                          #+#        #+#      #+#     #
#     Solved: 2024-09-26 06:14:28 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

L,W,H = map(int, input().split())
N = int(input())
cubes = {}
for _ in range(N):
    a,b = map(int, input().split())
    cubes[2**a] = b 
maxsize = max(cubes.keys())

q = [(L,W,H)]
ans = 0 

while q:
    l,w,h = q.pop()
    _max = min([l,w,h])
    size = maxsize
    
    while size > 0 and (size > _max or size not in cubes or not cubes[size]):
        size //= 2 

    if size == 0 or not cubes[size]:
        ans = -1 
        break 

    cubes[size] -= 1 
    ans += 1 
    if l > size:
        q.append((l-size, w, h))

    if w > size:
        q.append((size, w-size, h))

    if h > size:
        q.append((size,size,h-size))

print(ans)