#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 12100                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/12100                         #+#        #+#      #+#     #
#     Solved: 2024-02-07 16:38:17 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
def flatten(array):
    res = []
    for line in array:
        res += line 
    return tuple(res) 
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
def to_left(line):
    line = [el for el in line if el]
    line = line + [0] * (N-len(line))
    # merging 
    for i in range(N-1):
        if line[i] == line[i+1]:
            line[i] = line[i] * 2
            line[i+1] = 0
    line = [el for el in line if el]
    line = line + [0] * (N-len(line))
    return line
def to_right(line):
    return to_left(line[::-1])[::-1]
N = int(input().strip())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = set()
queue = deque([[arr, 0]])
flat_arr = flatten(arr)
max_cell = max(flat_arr)
visited.add(flat_arr)
while queue:
    arr, t = queue.popleft()
    if t == 5:
        break 
    transposed = transpose(arr)
    # state가 방향이 없음.
    left = [ to_left(line) for line in arr]
    right = [ to_right(line) for line in arr]
    up = [ to_left(line) for line in transposed]
    down = [ to_right(line) for line in transposed]
    for i, new_arr in enumerate([left, right, up, down]):
        hashed = flatten(new_arr)
        if hashed not in visited:
            visited.add(hashed)
            queue.append([new_arr, t+1])
            if max(hashed) > max_cell:
                max_cell = max(hashed)
print(max_cell)