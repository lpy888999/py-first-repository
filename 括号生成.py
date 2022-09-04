#递归
#递推 (a)b 式，ab是合规的括号串
#为什么没有重复？

def generateParenthesis(n: int)->list[str]:
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    ans = []
    for c in range(n):
        for i in generateParenthesis(c):
            for j in generateParenthesis(n-c-1):
                ans.append('({}){}'.format(i,j))
    return ans
print(generateParenthesis(3))
                
