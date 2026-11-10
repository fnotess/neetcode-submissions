class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        prod =1
        zero_count = 0

        #get zero count first if zero count more than 1 return all 0's
        #
        for num in nums:
            if num!=0:
                prod = prod*num
            else:
                zero_count = zero_count+1
        
        if zero_count>1:
            return [0]*len(nums)

        res = [0]*len(nums)

        for i,c in enumerate(nums):
            if zero_count!=0:
                if c!=0:
                    # if number pput 0
                    res[i]=0
                else:
                    # if zero put numbe rproduct 
                    res[i]=prod
            else:
                #no zeros in the list so just divide
                   res[i] = prod//c
        
        return res



        # product=1
        # my_list = [x for x in nums if x!=0]
        # print(my_list)

        # res =  math.prod(my_list)
        # print(res)

        # lst = []
        # for i in range(len(nums)):
        #     if nums[i]!= 0:
        #         if 0 in nums:
        #             lst.append(0)
        #         else:
        #             lst.append(int(res/nums[i]))
        #     else:
        #         lst.append(res)
        # return lst


        # lst = []
        # product =1
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             product =product *nums[j]
        #     lst.append(product)
        # # print(lst)
        # return lst