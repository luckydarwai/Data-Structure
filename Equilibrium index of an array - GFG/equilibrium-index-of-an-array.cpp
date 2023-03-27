//{ Driver Code Starts
#include <iostream>
using namespace std;
#include <stdio.h>
 
int findEquilibrium(int [], int );
 
int main() {
	int T;
	cin>>T;
	while(T--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		cout<<findEquilibrium (a,n)<<endl;
	}
	// your code goes here
	return 0;
}
// } Driver Code Ends


/* You are required to complete this method*/
int findEquilibrium(int A[], int n)
{
  //Your code here
  int leftsum=0,rightsum=0;
  for(int i=0;i<n;i++)
  {
      rightsum+=A[i];
  }
  
  
  for(int i=0;i<n;i++)
  {
      rightsum-=A[i];
      if(leftsum==rightsum)
      {
          return i;
      }
      leftsum+=A[i];
      
  }
  return -1;
}