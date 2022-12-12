'''
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
'''

'''Solution to find if there is a valid anagram passed in'''
class Solution:
    '''
    takes in 2 strings and first checks if the values are the same length, if they are
    then will move to for loop where we add the number of occurrences of each character to the 
    dictionary. 
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            # .get() is making 0 the default value to avoid a key error since that char would not be in the list
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
    def isAnagram2(self, s: str, t: str) -> bool:
        '''
        other option that is much simpler that sorted the two strings and then compares the sorted strings
        '''
        x = sorted(s)
        y = sorted(t)
        if x == y:
            return True
        else:
            return False

# sample data
s0 = "anagram"
t0 = "nagaram"
s1 = "rat"
t1 = "car"

# run sample data
s = Solution()
print(s.isAnagram(s0, t0))
print(s.isAnagram(s1,t1))
print(s.isAnagram2(s0, t0))
print(s.isAnagram2(s1, t1))