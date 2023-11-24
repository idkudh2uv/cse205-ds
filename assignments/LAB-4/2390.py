class Solution:
    def removeStars(self, s: str) -> str:
        new_s = ''

        for i in range(len(s)):
            if s[i] == '*':
                new_s = new_s[:len(new_s)-1]
            else:
                new_s = new_s + s[i]

        return new_s