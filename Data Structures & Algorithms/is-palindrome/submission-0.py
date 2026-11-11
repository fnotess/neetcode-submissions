class Solution:
    def isPalindrome(self, s: str) -> bool:

        print(s)
        x= "".join(char for char in s if char.isalnum())
        print(x)
        rev = s[::-1]
        print(rev)
        rev1= "".join(char for char in rev if char.isalnum())
        print(rev1)
        
        if rev1.lower()==x.lower():
            return True
        else:
            return False
        
