//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:

	int maxProduct(int arr[], int n) {
	   int max=0;
	   int sec_max=0;
	   for(int i=0;i<n;i++)
	   {
	       if(max<arr[i])
	       {
	           sec_max=max;
	           max=arr[i];
	       }
	       else if(sec_max<arr[i] )
	       {
	           sec_max=arr[i];
	       }
	   }
	   return max*sec_max;
	}
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int arr[n];
        for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.maxProduct(arr, n);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends