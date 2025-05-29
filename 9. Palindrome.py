class Solution(object):
    def isPalindrome(self, x):
        if '-' in str(x):
            return False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
