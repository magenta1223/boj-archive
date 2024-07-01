#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17387                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17387                         #+#        #+#      #+#     #
#     Solved: 2024-03-11 12:48:36 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
 
def solution():
    # ccw 1 -> 2 -> 3의 방향 결정 평행 0, 좌 -1, 우 1 
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)
    # 두 선분이 일직선상에 위치 
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        # -> mx1 <= mx3 <= mx2 <= mx4 or 
        #    mx3 <= mx1 <= mx4 <= mx2 
        # => mx1 <= mx4 and mx3 <= mx2 
        # x축에 수직한 경우도 고려해야 함 -> y도 추가 
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    # 교차 -> 반드시 만남 
    elif ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
        return 1
    
    # 한 선분의 모든 점이 다른 선분의 한 쪽에 위치 
    return 0
 
 
if __name__ == '__main__':
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))
    # A1, A2의 범위
    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    # B1, B2의 범위
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
    print(solution())