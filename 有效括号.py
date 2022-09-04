def isValid(s: str) -> bool:
    A = []
    for i in range(len(s)):
        if s[i] in {'(','{','[' }:#是左括号
            A.append(s[i])
        else:
            if A: #A 不为空且为右括号 成功匹配则消去，消去失败则括号不合法
                if s[i] == ')' and A[-1] == '(':
                    A.pop()
                elif s[i] == ']' and A[-1] == '[':
                    A.pop()
                elif s[i] == '}' and A[-1] == '{':
                    A.pop()
                else:
                    return False 
            else:#未能消去的右括号入栈
                A.append(s[i])
    return False if A else True   
B = ']'
print(isValid(B))
