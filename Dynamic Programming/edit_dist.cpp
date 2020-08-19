#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int min(int a, int b, int c){
    return min(min(a,b),c);
}
void editdistance(string s1, string s2){
    int m = s1.length()+1, n = s2.length()+1;
    int arr[m][n];
    if(s1.compare(s2) == 0)
        cout<<"0 operations";
    else{
        for(int i = 0; i<=m; i++){
            for(int j = 0; j<=n; j++){
                if(i == 0){
                    arr[i][j] = j;
                }
                else if(j == 0){
                    arr[i][j] = i;
                }
                else if(s1[i-1] == s2[j-1]){
                    arr[i][j] = arr[i-1][j-1];
                }
                else{
                    arr[i][j] = min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1])+1;
                }
            }
        }
        cout<<arr[m][n]<<" operations";
    }
}
int main(){
    string s1,s2;
    getline(cin,s1);
    getline(cin,s2);
    // cout<<s1.length()<<" "<<s2.length();
    editdistance(s1,s2);    
    return 0;
}