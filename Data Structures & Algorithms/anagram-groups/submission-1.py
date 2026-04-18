class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str) -> bool:
            freq1 = {}
            freq2 = {}
            
            for char in s:
                freq1[char] = freq1.get(char, 0) + 1

            for char in t:
                freq2[char] = freq2.get(char, 0) + 1

            return freq1 == freq2
        
        strs_copy = list(strs)
        solution = []

        while strs_copy:
            anagrams = []
            item = strs_copy.pop(0)
            anagrams.append(item)
            
            remaining = []
            for s in strs_copy:
                if isAnagram(item, s):
                    anagrams.append(s)
                else:
                    remaining.append(s)
            
            strs_copy = remaining
            solution.append(anagrams)

        return solution