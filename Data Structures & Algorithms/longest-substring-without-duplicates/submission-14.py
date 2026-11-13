class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lst = []
        max_len = 0

        left = 0

        

        for i in range(len(s)):
            curr = s[i]

            if curr not in lst:
                lst.append(curr)
                curr_len = len(lst)
                max_len = max(max_len,curr_len)
            else:
                curr_len = len(lst)
                max_len = max(max_len,curr_len)
                left= lst.index(curr)
                #print('left ' , left)
                del lst[:left+1]
                #print('lst before ' , lst)
                lst.append(curr)
                #print('left lst ' , lst, 'curr ', curr)
                # lst.clear()
                # lst.append(curr)
            
        return max_len