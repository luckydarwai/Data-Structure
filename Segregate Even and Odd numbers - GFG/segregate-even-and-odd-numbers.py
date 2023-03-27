#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr, n):
	    even=[arr[i] for i in range(n) if arr[i]%2==0]
	    odd=[arr[i] for i in range(n) if arr[i]%2!=0]
	    even.sort()
	    odd.sort()
	    a=even+odd
	   # print(a)
	    for i in range(n):
	        arr[i]=a[i]
	        
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends