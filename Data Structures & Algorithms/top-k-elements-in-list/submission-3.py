class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map ={}
        counts = Counter(nums)

        top_k= sorted(counts,key=counts.get,reverse=True)[:k]

        #ranked = sorted(counts,key=counts.get,reverse=True)
     
        return top_k

      
        