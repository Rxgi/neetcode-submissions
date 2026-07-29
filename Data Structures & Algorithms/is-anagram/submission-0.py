class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_reverse = t[::-1]
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        