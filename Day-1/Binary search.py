'''9. Checks if a given number x exists in a sorted array arr using binary search. Analyze its time complexity using Big-O notation.'''
def binarysearch(nums,key):
    nums.sort()
    print(nums)
    left=0
    right=len(nums)-1
    mid=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==key:
            return mid
        elif nums[mid]<key:
            left=mid+1
        else:
            right=mid-1
    return mid
nums=[3,4,6,-9,10,8,9,30]
key=10
print(binarysearch(nums,key))

Output:[-9, 3, 4, 6, 8, 9, 10, 30]
6
