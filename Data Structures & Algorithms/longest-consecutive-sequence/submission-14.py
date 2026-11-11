class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,2,5,4,6,1,1]
        # 0,1,1,2,3,4,5,6

        lst = sorted(set(nums))
        #print(lst)

        consecutive_count = 0
        prev_value =0
        max_consecutive_count=0

        if len(nums)==1 or len(set(nums))==1:
            return 1

        for i,c in enumerate(lst):
            if i == 0:
                prev_value= c
                consecutive_count = consecutive_count+1
                #print("first",prev_value,consecutive_count)
            else:
                if prev_value==c:
                    #print("y")
                    continue
                elif prev_value+1==c:
                    prev_value= c
                    consecutive_count = consecutive_count + 1
                    #print("x" ,prev_value,consecutive_count)
                    if consecutive_count>max_consecutive_count:
                       max_consecutive_count =consecutive_count
                else:
                    if consecutive_count> max_consecutive_count:
                        max_consecutive_count = consecutive_count
                        #print("max", max_consecutive_count)

                    consecutive_count=1
                    prev_value=c


        return max_consecutive_count

            

