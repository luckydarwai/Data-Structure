#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        
        # for i in range(n):
        #     if arr.count(arr[i])==1:
        #         return arr[i]
        # return 0
        
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=0
            else:
                dic[i]+=1
        # print(dic)
        for i in arr:
            if dic[i]==0:
                return i
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends