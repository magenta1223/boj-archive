#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1450                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1450                          #+#        #+#      #+#     #
#     Solved: 2024-02-05 17:20:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def subset(arr: list, max_sum: int):
    result = []
    # 비트마스킹. -> array의 모든 부분집합을 indexing함. 
    # 0: 000 (아무 요소도 포함하지 않음)
    # 1: 001 (c만 포함)
    # 2: 010 (b만 포함)
    # 3: 011 (b, c 포함)
    # 4: 100 (a만 포함)
    # 5: 101 (a, c 포함)
    # 6: 110 (a, b 포함)
    # 7: 111 (a, b, c 모두 포함)
    for i in range(1 << len(arr)):
        sub_sum = 0
        is_over = False
        for j in range(len(arr)):
            # 아무요소도 포함하지 않는 경우를 제외, 
            # 1 << j는 숫자 1을 j 비트만큼 왼쪽으로 시프트합니다. 이는 2^j의 값을 갖습니다.
            # 예를 들어, j가 2라면 1 << 2는 100(2진수)이며, 이는 4(10진수)와 같습니다.
            # i & (1 << j)는 i의 j번째 비트가 1인지를 검사합니다.
            # 만약 j번째 비트가 1이라면, i & (1 << j)의 결과는 0이 아니게 되고, 이는 if 조건문에서 참(True)으로 평가됩니다.
            # 반면, j번째 비트가 0이라면, 결과는 0이 되고, 이는 거짓(False)으로 평가됩니다.
 
            # 즉 현재 조합을 의미하는 i가 j번째 요소를 포함하는 경우라면 그 값을 sub_sum에 추가 
            if i & (1 << j):
                sub_sum += arr[j]
                # 그 값이 최대치를 넘긴다면 의미가 없음. 제외 
                if sub_sum > max_sum:
                    is_over = True
                    break
        if not is_over:
            result.append(sub_sum)
    # 즉. 가능한 모든 부분집합에 대해, 값이 C 이하인 모든 조합을 list로 갖게됨. 
    result.sort()
    return result
 
N, C = map(int, input().split())
arr = list(map(int, input().split()))
# 두 리스트로 나눠서 사용
arr1, arr2 = arr[:N // 2], arr[N // 2:]
subset1 = subset(arr1, C)
subset2 = subset(arr2, C)
 
a, b = 0, len(subset2) - 1
ans = 0
while a < len(subset1) and b >= 0:
    s = subset1[a] + subset2[b]
    if s > C:
        b -= 1
    else:
        a += 1
        ans += b+1 
print(ans)