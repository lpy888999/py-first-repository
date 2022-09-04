#动态规划 串长度遍历：2->len(A)
         # 结果储存在二维数组中 de[i][j]?=True 可用于判断 de[i-1][j+1]
#中心扩展法
class Solution:
    def expand(self,s: str,left: int,right: int) -> int:
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1

    def longestPalindrome(self, s: str) -> str:
        start,end = 0,0
        
        for i in range (len(s)):#遍历一遍，n
            left1,right1 = self.expand(s,i,i) #中心为一个数
            if i < len(s)-1:
                left2,right2 = self.expand(s,i,i+1)#中心为两个数
            if right1 - left1 > end - start:
                start,end = left1,right1
            if right2 - left2 > end - start:
                start,end = left2,right2
        return s[start:end+1]

S=Solution()
print(S.longestPalindrome(s='babad'))           

