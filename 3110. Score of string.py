class Solution(object):
    def scoreOfString(self, s):
        ascii_value = [ord(c) for c in s]
        score = 0
        for i in range(len(ascii_value) - 1):
            sum = abs(ascii_value[i] - ascii_value[i+1])
            score += sum
        print(score)

sol = Solution()
sol.scoreOfString("hello")