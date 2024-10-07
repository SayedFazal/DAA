'''You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values: answer1 : the number of indices i such that nums1[i] 
exists in nums2. answer2 : the number of indices i such that nums2[i] exists in nums1 Return [answer1,answer2]'''
def calculate_values(nums1, nums2):
    set_nums2 = set(nums2)
    set_nums1 = set(nums1)
    answer1 = sum(1 for num in nums1 if num in set_nums2)
    answer2 = sum(1 for num in nums2 if num in set_nums1)
    return answer1, answer2
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 3, 4, 5, 6]
result = calculate_values(nums1, nums2)
print("answer1:", result[0], "answer2:", result[1])
#Output: answer1: 4 answer2: 3
