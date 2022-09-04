def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    all = sorted(nums1+nums2)#sorted()函数会返回一个列表，而sort（）函数是直接在原来的基础上修改:list.sort()，其次注意语法)
    m = len(nums1)
    n = len(nums2)
    if (m+n) % 2 == 0: return (all[(m+n)//2-1]+all[(m+n)//2])/2
    else: return all[(m+n+1)//2-1]
a = findMedianSortedArrays([1,3],[2])
print(a)
