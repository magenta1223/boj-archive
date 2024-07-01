#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1780                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1780                          #+#        #+#      #+#     #
#     Solved: 2023-12-21 18:07:45 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def check_same(array, x1, y1, x2, y2):
    initial = array[x1][y1]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if array[i][j] != initial:
                return False, None
    return True, initial
 
def split_indices(n):
    n_third = n // 3
    for i in range(0, n, n_third):
        for j in range(0, n, n_third):
            yield (i, j, i + n_third, j + n_third)
 
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
 
queue = [(0, 0, N, N)]
count = {0: 0, 1: 0, -1: 0}
 
while queue:
    x1, y1, x2, y2 = queue.pop()
    is_same, val = check_same(array, x1, y1, x2, y2)
    if is_same:
        count[val] += 1
    else:
        for indices in split_indices(x2 - x1):
            queue.append((x1 + indices[0], y1 + indices[1], x1 + indices[2], y1 + indices[3]))
 
print(count[-1])
print(count[0])
print(count[1])
 