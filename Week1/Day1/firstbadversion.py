class Solution(object):
    def firstBadVersion(self, n):
        if n==1:
            return n
        start = 1
        end = n
        while start <= end:
            mid = int((start+end)/2)
            if(isBadVersion(mid)==True and isBadVersion(mid-1)==False):
                return mid
            elif(isBadVersion(mid-1)==True):
                end = mid - 1
            else:
                start = mid + 1
