class Solution:
    # Time complexity: O(n) where n is the length of the input string
    # Space complexity: O(1) since the dictionary has never more than 26 elements
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        left = 0
        have = dict()
        
        for right, el in enumerate(s):
            if el in have:
                left = max(left, have[el]+1)
            max_sub = max(max_sub, right - left + 1)
            have[el] = right
        return max_sub
