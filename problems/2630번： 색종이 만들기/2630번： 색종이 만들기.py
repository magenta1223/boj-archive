#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2630                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2630                          #+#        #+#      #+#     #
#     Solved: 2023-12-21 17:26:29 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def check_split(array):
    s = sum([sum(a) for a in array])
    n = len(array)
    n_half = n // 2
    if s == n ** 2:
        return True, True, None    
    elif s == 0:
        return True, False, None
    else:        
        new_arrays = [[[0 for _ in range(n_half)] for _ in range(n_half)] for _ in range(4)]
        
        for i in range(n):
            subar_i = i // n_half
            new_i = i%n_half
            for j in range(n):
                subar_j = j // n_half
                new_j = j%n_half
                new_arrays[subar_i * 2 + subar_j][new_i][new_j] = array[i][j]
        return False, None, new_arrays
 
N=int(input())
array = [ list(map(int, input().split())) for _ in range(N)]
 
from collections import deque
 
countOne = 0
countZero =0
 
queue = deque([array])
while queue:
    _arr = queue.popleft()    
    isSame, isOne, newArr = check_split(_arr)
    if isSame:
        if isOne:
            countOne+=1
        else:
            countZero+=1
    else:
        queue.extend(newArr)
print(countZero)
print(countOne)