class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        dict={} # create an empety dictionary
        for i in range (len(nums)): # go through each item in the list
            if nums[i] in dict: # if item found in dist return the result
                return [dict[nums[i]],i]
            else: # if the number is not in the dict add "target-item" : item
                dict[target-nums[i]]=i
"""                
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
                
