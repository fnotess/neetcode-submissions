class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count=0
        length= len(nums)
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i]= 1
        return False

        