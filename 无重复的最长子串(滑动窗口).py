class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
            
        i,j=0,1
        max_len=0
        tmp_len=0
        if len(s):
            hashset.add(s[0])
            max_len=1
        # print(len(s))
        while j<len(s):
            # print(j,s[j])
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            hashset.add(s[j])
            tmp_len=j-i+1
            if tmp_len>max_len:
                max_len=tmp_len
            j+=1
        return max_len
            
        
