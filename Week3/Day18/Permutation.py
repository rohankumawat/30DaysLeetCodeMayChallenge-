class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_len = len(s1)
        s1_count = Counter(s1)
        win_count = Counter()
        for i, c in enumerate(s2):
            win_count[c] += 1
            if i >= s1_len:
                left_element = s2[i - s1_len]
                if win_count[left_element] == 1:
                    del win_count[left_element]
                else:
                    win_count[left_element] -= 1
            if win_count == s1_count:
                return True
        return False
