
def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_volume = 0
    while left != right:
        tmp_v = (right - left) * min(height[left],height[right])
        if tmp_v > max_volume: max_volume = tmp_v
        if height[left]<height[right]:
            left+=1
        else: right-=1
    return max_volume
M=maxArea([1,1])
print(M)


