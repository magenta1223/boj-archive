#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17140                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17140                         #+#        #+#      #+#     #
#     Solved: 2024-02-18 17:35:19 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter
 
r,c,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(3)]
 
# 행연산
def sort_row(row):
    # Counter 
    c = Counter(row)
    # 0제외 
    del c[0]
    # number, frequency
    # 빈도, 숫자 오름차순 정렬 
    next_row = []
    for n, f in sorted([(n,f) for n, f in c.items()], key=lambda x : (x[1], x[0])):
        next_row.extend([n,f])   
    return next_row 
 
def zfill_row(row, target_len):
    zfill = row + [0] * (target_len - len(row))
    return zfill[:100]
    
def R(array):
    array = [sort_row(row) for row in array]
    target_len = max([len(row) for row in array])
    return [zfill_row(row, target_len) for row in array]
 
def C(array):
    array = R([list(col) for col in zip(*array)])
    return [list(row) for row in zip(*array)]
 
def oper(array):
    return R(array) if len(array) >= len(array[0]) else C(array)
 
r-=1
c-=1
ans = 101
for t in range(101):
    if len(A) > r and len(A[0]) > c and A[r][c] == k:
        ans = t
        break 
    A=oper(A)
 
print(ans if ans <= 100 else -1)