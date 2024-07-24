#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1918                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1918                          #+#        #+#      #+#     #
#     Solved: 2024-07-24 05:23:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


S = input()
def infix_to_postfix(expression:str):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []  # 연산자를 저장할 스택
    output = []  # 후위 표기식 결과를 저장할 리스트
    for char in expression:
        # 피연산자는 결과에 추가
        if char.isalnum():
            output.append(char)
        # 왼쪽 괄호는 스택에 추가
        elif char == '(':
            stack.append(char)
        # 오른쪽 괄호는 왼쪽 괄호를 만날 때까지 스택에서 팝하여 결과에 추가
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # 왼쪽 괄호 제거

        # 연산자는 우선순위에 따라 스택에서 팝하여 결과에 추가 후 스택에 추가
        else:
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
        # print(stack)
        # print(output)
        # print('--------------------')
    # 스택에 남아 있는 모든 연산자를 결과에 추가
    while stack:
        output.append(stack.pop())

    return ''.join(output)


print(infix_to_postfix(S))