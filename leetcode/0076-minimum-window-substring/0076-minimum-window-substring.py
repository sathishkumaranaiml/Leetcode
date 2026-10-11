class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

    # Frequency map for t
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        required = len(t_count)  # Distinct chars in t that must be satisfied
        formed = 0               # Distinct chars currently meeting required freq
        window_count = {}

        best_start, best_len = 0, float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window_count[c] = window_count.get(c, 0) + 1

        # Check if this character's frequency requirement is now met
            if c in t_count and window_count[c] == t_count[c]:
                formed += 1

        # Shrink the window from the left while it remains valid
            while formed == required:
                if right - left + 1 < best_len:
                    best_start = left
                    best_len = right - left + 1

                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]
        
