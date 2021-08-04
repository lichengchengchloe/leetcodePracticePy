# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
import random
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    k = len(nums)-k
    kth_index = quick_sort(nums,k,0,len(nums)-1)
    return nums[kth_index]

def quick_sort(nums,k,left,right):
    j = partition(nums,left,right)
    if j==k:
        return j
    elif j<k:
        return quick_sort(nums,k,j+1,right)
    elif j>k:
        return quick_sort(nums,k,left,j-1)

def partition(nums,left,right):
    random_index = random.randint(left,right)
    nums[left],nums[random_index] = nums[random_index],nums[left]
    pivot = nums[left]
    while left<right:
        while pivot<nums[right] and left<right:
            right-=1
        nums[left], nums[right] = nums[right], nums[left]
        while pivot>=nums[left] and left<right:
            left+=1
        nums[left],nums[right] = nums[right],nums[left]

    return left

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
