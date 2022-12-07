'''
Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


'''solution for Two Sum'''
class Solution:

    '''Loop over the array of nums looking each time if the difference in the current value
    minus the target is in the dictionary. Once we find that the difference is in the dictionary,
    then return the current index and the index of the difference. '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# sample data
nums = [2,7,11,15]
target = 9

# run sample data
s = Solution()
print(s.twoSum(nums, target))