#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 4779                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/4779                          #+#        #+#      #+#     #
#     Solved: 2023-11-24 16:53:09 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def func(strs):
    if strs == " "*len(strs):
        return strs 
    else:
        unit=len(strs) // 3
        _strs = "-"*unit + " " * unit + "-"*unit
        if unit == 1:
            return _strs
        elif unit ==0:
            return strs
        else:
            return func(_strs[:unit]) + func(_strs[unit:-unit]) + func(_strs[-unit:])
try:
    while True:
        N=int(input())
        strs = "-"*(3**N)
        print(func(strs))
except:
    pass