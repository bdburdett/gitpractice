'''Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.
'''

'''solution to contains duplicate'''
class Solution:
    '''
    loops through nums and checks if current value is in the set. If it is not then it will add it. If it is then it will 
    immediately return false. Sets cannot contain duplicates.
    '''
    def containsDuplicate(self, nums: list[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# sample data
nums0 = [1,2,3,1]
nums1 = [1,2,3,4]
nums2 = [1,1,1,3,3,4,3,2,4,2]

# run sample data
s = Solution()
print(s.containsDuplicate(nums0))
print(s.containsDuplicate(nums1))
print(s.containsDuplicate(nums2))
