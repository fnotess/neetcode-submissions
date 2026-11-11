class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i >0 and nums[i]== nums[i-1]:
                continue

            target = -nums[i]
            left = i+1
            right = len(nums)-1

            while left <right:
                pair_sum = nums[left] + nums[right]

                if pair_sum <target:
                    left =left+1

                elif pair_sum >target:
                    right = right-1

                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left = left+1
                    right= right-1

                    while left<right and nums[left]== nums[left-1]:
                        left = left+1
                    while left<right and nums[right]== nums[right+1]:
                        right = right-1
        
        return result
                