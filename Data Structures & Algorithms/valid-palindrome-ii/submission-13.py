
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def ispali(a, b):
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return ispali(i + 1, j) or ispali(i, j - 1)

        return True