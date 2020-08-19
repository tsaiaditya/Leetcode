#include<iostream>
#include<stdlib.h>
using namespace std;
int minpart(int arr[], int n){
    if(n == 0)
        return -1;
    int totalsum = 0;
    for(int i = 0; i<n; i++)
        totalsum+= arr[i];
    int searchsum = totalsum/2;
    bool dp[n][searchsum+1];
    for(int i = 0; i<n; i++){
        for(int j = 0; j<=searchsum; j++)
            dp[i][j] = false;
    }
    for(int i = 0; i<n; i++){
        dp[i][0] = true;
    }
    for(int i = 0; i<=searchsum; i++){
        if(i == arr[0])
            dp[0][i] = true;
    }
    for(int i = 1; i<n; i++){
        for(int j = 1; j<=searchsum; j++){
            if(dp[i-1][j])
                dp[i][j] = true;
            else{
                if(j>=arr[i])
                    dp[i][j] = dp[i-1][j-arr[i]];
            }
        }
    }
    int partition1 = -1;
    for(int j = searchsum; j>=0; j--){
        if(dp[n-1][j]){
            partition1 = j;
            break;
        }
    }
    int partition2 = totalsum - partition1;
    return abs(partition1-partition2);
}
int main(){
    int n;
    cout<<"Enter length of array: ";
    cin>>n;
    int arr[n]={};
    cout<<"Enter array elements: "<<endl;
    for(int i = 0; i<n; i++)
        cin>>arr[i];
    int res = minpart(arr,n);
    if(res!=-1)
        cout<<"The mimimum difference between sum of 2 sets is : "<<res;
    else
        cout<<"Invalid input";
    return 0;
}