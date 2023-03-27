#User function Template for python3

class Solution:
    def __init__(self):
        self.cache = {}

    def dp(self, nxt, summ, n):
        if summ == 0 and n == 0:
            return 1
        if summ <= 0 or n == 0:
            return 0
        if (nxt, summ, n) in self.cache:
            return self.cache[(nxt, summ, n)]
        ans = 0
        for i in range(1, nxt+1):
            ans += self.dp(i, summ-i, n-1)
        self.cache[(nxt, summ, n)] = ans
        return ans

    def countWaystoDivide(self, N, K):
        ans = 0
        for i in range(1, N+1):
            ans += self.dp(i, N-i, K-1)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(1000000)

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        K=int(input())
        ob = Solution()
        print(ob.countWaystoDivide(N,K))
        
        T -= 1
# } Driver Code Ends