'''Sort an array of integers using the bubble sort technique. Analyze its time complexity using Big-O notation. Write the code'''
def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(1,len(nums)-i):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
    return nums
nums=[10,30,20,15]
print(bubble_sort(nums))
Output:[10, 15, 20, 30]
