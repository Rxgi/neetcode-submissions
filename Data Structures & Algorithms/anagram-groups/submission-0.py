class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        for x in strs:
            sorted_str = "".join(sorted(x))
            
            if sorted_str not in hash_map:
                hash_map[sorted_str] = []
            hash_map[sorted_str].append(x)        
        
        return list(hash_map.values())

