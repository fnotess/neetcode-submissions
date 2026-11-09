class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        if len(strs)==1:
            return [[strs[0]]]
        if len(strs)==0:
            return [[""]]

        for index,value in enumerate(strs):
            value_sorted = ''.join(sorted(value))
            if value_sorted in map:
                map[''.join(sorted(value))].append(value)
            else:
                 map[''.join(sorted(value))]= [value]
        
        return list(map.values())


        