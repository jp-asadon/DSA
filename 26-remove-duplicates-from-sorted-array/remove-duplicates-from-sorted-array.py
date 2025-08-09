class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        new_list = []
        for i in nums:
            if i not in new_list:
                new_list.append(i)
                nums[k] = i
                k+=1
        return k
        
solution = Solution()
nums = sorted([0,0,1,1,1,2,2,3,3,4])
result = solution.removeDuplicates(nums)
print(result)