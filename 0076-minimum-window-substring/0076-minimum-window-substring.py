class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        left = 0
        min_length = float('inf')
        substring = ""
        target_length = len(t)
        
        for right in range(len(s)):
            # if we find a letter in t
            if target_counter[s[right]] > 0:
                target_length -= 1
            
            target_counter[s[right]] -= 1
            
            # if the sliding window is valid, i.e. we find all letters in t
            while target_length == 0:
                len_window = right - left + 1
                
                if not substring or len(substring) > len_window:
                    substring = s[left: right + 1]
                
                # move the window one step to the right
                target_counter[s[left]] += 1
                
                # if s[left] is a letter in t
                # we need to break the while loop
                if target_counter[s[left]] > 0:
                    target_length += 1
                
                left += 1
            
        return substring