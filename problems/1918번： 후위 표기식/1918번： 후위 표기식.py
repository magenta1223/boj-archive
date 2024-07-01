#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1918                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1918                          #+#        #+#      #+#     #
#     Solved: 2024-03-06 14:07:42 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

EQ = input().strip() 
 
def solve_oper(eq, operators):
    postfix_eq, i = [], 0 
    while i < len(eq):
        if eq[i] in operators:
            postfix_eq[-1] = postfix_eq[-1] + eq[i+1] + eq[i]
            i += 1
        else:
            postfix_eq.append(eq[i])
        i += 1    
    return postfix_eq
 
def solve(eq):
    eq, i, end = list(eq), 0, len(eq)
    add, mul = ['+', '-'], ['*', '/']
    while i < end:
        if eq[i] == ")":
            # find left
            j = i 
            while eq[j] != '(':
                j -= 1
            # solve eq[j:i] except for bracket
            eq = eq[:j] + solve_oper(solve_oper(eq[j+1:i], mul), add) + eq[i+1:]
            end = len(eq)
            i = j
        i += 1
    return solve_oper(solve_oper(eq, mul), add)[0]
print(solve(EQ))