#include<iostream> 
using namespace std; 

int printCountDP(int dist) 
{ 
	int count[dist+1]; 
	count[0] = 1, count[1] = 1, count[2] = 2; 
	for (int i=3; i<=dist; i++) 
	    count[i] = count[i-1] + count[i-2] + count[i-3]; 
	return count[dist];
} 

int main() 
{ 
	int dist;
    cout<<"Enter number of steps: ";
    cin>>dist; 
	cout << "Number of ways to cover the distance with 1, 2 and 3 steps: " << printCountDP(dist); 
	return 0; 
} 
