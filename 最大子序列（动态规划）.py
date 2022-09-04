L=[2,-3,3,-50]
s=[0 for i in range(len(L))]
print(s)
s[0]=L[0]
for i in range(1,len(s)):
 if s[i-1]>=0:             #动态规划，从只有一个元素的列表开始
                           #如果之前的 可能最大连续子列值 加上新的一个元素不会使其变小（之前的 可能最大子列值非负）
        s[i]=s[i-1]+L[i]   #得到新的 可能最大连续子列 值
 else:
        s[i]=L[i]          #否则就用新元素本身
print(s)
print(max(s))