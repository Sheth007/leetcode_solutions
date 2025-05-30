class Solution(object):
    def differenceOfSums(self, n=10, m=3):
        i = 0
        sum_div = 0
        sum_non_div = 0
        while i < n:
            i+=1
            if(i % m ==0):
                sum_div += i
            else:
                sum_non_div += i
        return sum_non_div - sum_div