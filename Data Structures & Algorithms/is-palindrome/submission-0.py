class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = ""

        for ch in s:
            if ch.isalnum():
                cleared += ch.lower()
        return cleared == cleared [:: -1]