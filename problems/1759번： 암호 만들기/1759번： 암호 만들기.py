#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1759                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1759                          #+#        #+#      #+#     #
#     Solved: 2024-07-31 04:45:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 암호로 동작하는 시스템 
# 암호는
# 1. L개의 unique한 알파벳 소문자로 구성
# 2. 최소 한 개의 모음
# 3. 최소 2개의 자음 
# 암호는 오름차순으로 구성 

# 문자로 사용했을법한 문자는 C개 존재. 
# 가능성 있는 암호를 모두 구해보자 

# 최대 binom{15, 7} = 15

# 걍 모든 조합 구하고 
# 모음 1개 자음 2개 안되는거 제끼면 됨 

from itertools import combinations 

VOWELS = 'aeiou'

def check(password):
    a = sum([ ab in VOWELS  for ab in password])
    return True if a>=1 and L-a >=2 else False 
L,C = map(int, input().split())
S = sorted(input().split())
passwords = ["".join([S[i] for i in comb]) for comb in combinations(list(range(C)), L)]
for password in passwords:
    if check(password):
        print(password)