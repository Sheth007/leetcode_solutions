class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        count = 0
        for ch in stones:
            if ch in jewels:
                count += 1
        return count
            