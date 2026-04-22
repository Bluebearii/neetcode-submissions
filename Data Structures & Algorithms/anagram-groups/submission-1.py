class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        isAnagram = {}
        for i,string in enumerate(strs):
            key = "".join(sorted(string))
            
            if key not in isAnagram:
                isAnagram[key] = []
            isAnagram[key].append(string)
        return list(isAnagram.values())