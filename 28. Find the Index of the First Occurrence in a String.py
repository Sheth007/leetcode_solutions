class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack :
            new = haystack.index(needle)
            return(new)
        else:
            return -1