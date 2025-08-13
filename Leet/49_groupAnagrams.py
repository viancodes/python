from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort characters in the word to create a key
            key = tuple(sorted(word))  # tuple is hashable
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
