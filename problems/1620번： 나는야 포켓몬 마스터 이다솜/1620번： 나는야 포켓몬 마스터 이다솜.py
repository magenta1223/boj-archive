#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1620                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1620                          #+#        #+#      #+#     #
#     Solved: 2023-11-02 14:00:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = sys.stdin.readline
 
 
# 도감에 수록된 포켓몬의 개수 N과 문제의 개수 M을 입력받는다
N, M = map(int, input().split())
 
# 포켓몬의 이름을 저장할 딕셔너리 두 개를 생성한다
name_to_number = {}
number_to_name = {}
 
# 포켓몬의 이름을 입력받아 딕셔너리에 저장한다
for number in range(1, N + 1):
    name = input().strip()
    name_to_number[name] = number
    number_to_name[number] = name
 
# 문제를 해결하는 부분
for _ in range(M):
    query = input().strip()  # 문제(쿼리)를 입력받는다
 
    # 입력받은 쿼리가 숫자인 경우, 해당 포켓몬의 이름을 출력한다
    if query.isdigit():
        print(number_to_name[int(query)])
    # 입력받은 쿼리가 문자열인 경우, 해당 포켓몬의 번호를 출력한다
    else:
        print(name_to_number[query])
 