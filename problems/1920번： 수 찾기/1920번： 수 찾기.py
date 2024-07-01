#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1920                          #+#        #+#      #+#     #
#     Solved: 2023-12-26 12:28:40 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
A=list(map(int, input().split()))
M=int(input())
B=list(map(int, input().split()))
 
def search(array, num):
    _min, _max = 0, len(array) - 1
    while _min <= _max:
        _mid = (_min + _max) // 2
        if array[_mid] == num:
            return True 
        elif array[_mid] < num:
            _min = _mid + 1
        else:
            _max = _mid - 1        
    return False 
 
A = sorted(A)
for b in B:
    print(1 if search(A, b) else 0)