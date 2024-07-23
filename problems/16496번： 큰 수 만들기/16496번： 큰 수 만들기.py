#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 16496                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/16496                         #+#        #+#      #+#     #
#     Solved: 2024-07-23 08:08:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# A안의 수를 이어붙여서 가장 큰 수를 만들기 
# 모든 숫자를 10자리가 될 때 까지 반복한 수를 기준으로 역정렬 (#1422, #2385) (= #21479, #29119)

def fill(string):
    return int((string + string * 10)[:10])
N = int(input())
A = [(num, fill(num)) for num in input().split()]
A.sort(reverse= True, key = lambda x:x[1])
print(int("".join([num for num, v in A])))

