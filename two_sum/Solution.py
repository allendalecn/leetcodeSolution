"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]
            if x in dic:
                if dic[x] != i:
                    return [i,dic[x]]

    def binarySearch(self,sortedNums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        midIndex = math.floor(len(sortedNums) / 2)
        if midIndex == len(sortedNums) -1 or sortedNums[midIndex] == target or (sortedNums[midIndex -1] < target and sortedNums[midIndex] > target):
            return midIndex
        if sortedNums[midIndex] > target:
           sortedNums = sortedNums[0:midIndex]
           return self.binarySearch(sortedNums,target)
        else:
            sortedNums = sortedNums[midIndex:len(sortedNums)-1]
            return self.binarySearch(sortedNums,target)
        return midIndex

s = Solution()
print(s.twoSum([3,2,4],6))

#a = sorted([2,3,1,5,3,4,7,4])
#print(a)

                    
        