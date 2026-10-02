class Solution:  
    # Time complexity: O(n) where n is the length of the input string
    # Space complexity: O(1) since the set has never more than 26 elements
    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_sub = 0
        left = 0
        have = set()
        
        for right, el in enumerate(s):
            while el in have:
                have.remove(s[left])
                left += 1
            have.add(el)
            max_sub = max(max_sub, right - left + 1)
        return max_sub
