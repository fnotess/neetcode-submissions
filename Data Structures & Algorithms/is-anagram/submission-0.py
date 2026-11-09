class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        #countS = {}
        # countT = {}
        # for i in range(len(s)):
        #     current_letter = s[i]
        #     countS[current_letter] = countS.get(s[i])
        #     countS[current_letter] = 
        
        
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)
       
        if(sorted_s==sorted_t):
            return True
        return False