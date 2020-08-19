/*
Q- Given a positive integer n, find the least number of perfect square numbers which sum to n.
*/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int numSquares(int n) {
        vector<int> c(n+1,n);
        c[0] = 0;
        c[1] = 1;
        for(int i = 2; i<=n; i++){
            for(int j = 1; j*j<=i; j++){
                c[i] = min(c[i],c[i-j*j]+1);
            }
        }
        for(int i = 0; i<=n; i++)
            cout<<c[i]<<" ";
        cout<<endl;
        return c[n];
    }
};

int main(int argc, const char** argv) {
    Solution s;
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    cout<<"Number of perfect squares required for getting the sum given number : "<<s.numSquares(n);
    return 0;
}